"""Local demonstration with fictional data. No external services are called."""
import json

ALLOWED_FIELDS = ("experience", "qualifications", "start_in_days")

samples = {
    "separate_fields": {
        "name": "Fictional Applicant",
        "email": "applicant@example.invalid",
        "salary_expectation": 28000,
        "health_note": "I have asthma.",
        "experience": "Two years in warehouse operations.",
        "qualifications": "Forklift certificate",
        "start_in_days": 15,
    },
    "mixed_free_text": {
        "experience": "Two years in warehouse operations. I have asthma.",
        "qualifications": "Forklift certificate",
        "start_in_days": 15,
    },
}


def build_payload(application):
    return {field: application[field] for field in ALLOWED_FIELDS}


for label, application in samples.items():
    payload = build_payload(application)
    print(json.dumps({
        "case": label,
        "input": application,
        "proposed_payload": payload,
        "fictional_health_text_present": "I have asthma." in json.dumps(payload),
    }))
