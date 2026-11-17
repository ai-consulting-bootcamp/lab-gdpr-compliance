"""Synthetic lab proof: check for missing pre-close human review, never rank applicants."""
import argparse
import json
from datetime import datetime
from pathlib import Path


def timestamp(value):
    time = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if time.utcoffset() is None:
        raise ValueError("Timestamps require explicit offsets")
    return time


def check(data):
    closed = timestamp(data["shortlist_closed_at"])
    reviewed, blocked = [], {}
    seen = set()
    for application in data["applications"]:
        token = application["token"]
        if token in seen:
            raise ValueError("Duplicate application token")
        seen.add(token)
        if not application["eligible"]:
            continue
        review = application.get("review") or {}
        findings = []
        if not review.get("reviewer_id"):
            findings.append("NO_REVIEWER")
        if not str(review.get("reason") or "").strip():
            findings.append("NO_REVIEW_REASON")
        if not review.get("at"):
            findings.append("NO_REVIEW_TIMESTAMP")
        elif timestamp(review["at"]) >= closed:
            findings.append("REVIEW_NOT_BEFORE_CLOSE")
        if findings:
            blocked[token] = findings
        else:
            reviewed.append(token)
    return {
        "case": data["synthetic_case"],
        "vacancy": data["vacancy"],
        "reviewed_before_close": reviewed,
        "blocked_applications": blocked,
        "result": "BLOCK_AI_SHORTLIST" if blocked else "REVIEW_RECORDS_PRESENT",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()
    result = check(json.loads(args.fixture.read_text(encoding="utf-8")))
    print(json.dumps(result, indent=2))
    return 2 if result["blocked_applications"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
