import os
import sys
import json

from src.csv_parser import parse_csv
from src.pdf_parser import parse_pdf
from src.docx_parser import parse_docx
from src.detector import detect_resume_type

from src.extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_experience
)

from src.normalizer import (
    normalize_email,
    normalize_phone,
    normalize_skills
)

from src.matcher import match_candidate
from src.merger import merge
from src.projector import project
from src.validator import validate

csv_path = "input/candidates.csv"
resume_folder = "input/resumes"
output_folder = "output"

if len(sys.argv) == 4:
    csv_path = sys.argv[1]
    resume_folder = sys.argv[2]
    output_folder = sys.argv[3]

elif len(sys.argv) != 1:
    print("\nUsage:")
    print("python main.py")
    print("\nOR\n")
    print(
        "python main.py <csv_file> <resume_folder> <output_folder>"
    )
    sys.exit()

if not os.path.exists(csv_path):
    print(f"CSV file not found: {csv_path}")
    sys.exit()

if not os.path.exists(resume_folder):
    print(f"Resume folder not found: {resume_folder}")
    sys.exit()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

csv_candidates = parse_csv(csv_path)

matched_emails = set()

for file in os.listdir(resume_folder):

    if file.startswith("~$"):
        continue

    if not (
        file.endswith(".pdf")
        or file.endswith(".docx")
    ):
        continue

    path = os.path.join(
        resume_folder,
        file
    )

    file_type = detect_resume_type(path)

    try:

        if file_type == "pdf":
            text = parse_pdf(path)

        elif file_type == "docx":
            text = parse_docx(path)

        else:
            continue

    except Exception as e:

        print(
            f"Error reading {file}: {e}"
        )

        continue

    email_list = extract_email(text)

    phone_list = extract_phone(text)

    resume = {

        "name":
        extract_name(text),

        "email":
        normalize_email(
            email_list[0]
        )
        if email_list
        else None,

        "phone":
        normalize_phone(
            phone_list[0]
        )
        if phone_list
        else None,

        "skills":
        normalize_skills(
            extract_skills(text)
        ),

        "experience":
        extract_experience(text)
    }

    candidate = match_candidate(
        csv_candidates,
        resume
    )

    if not candidate:

        candidate = {
            "full_name": None,
            "email": None,
            "phone": None
        }

        print(
            f"Resume-only candidate: {resume['name']}"
        )

    else:

        if candidate["email"]:

            matched_emails.add(
                candidate["email"].lower()
            )

    profile = merge(
        candidate,
        resume
    )

    errors = validate(profile)

    if errors:
        print(
            f"Warning: {errors}"
        )

    with open(
        "config/default_config.json"
    ) as f:

        config = json.load(f)

    result = project(
        profile,
        config
    )

    if resume["email"]:

        filename = (
            resume["email"]
            .split("@")[0]
        )

    elif resume["name"]:

        filename = (
            resume["name"]
            .replace(" ", "_")
        )

    else:

        filename = (
            os.path.splitext(file)[0]
        )

    output_path = os.path.join(
        output_folder,
        filename + ".json"
    )

    with open(
        output_path,
        "w"
    ) as f:

        json.dump(
            result,
            f,
            indent=4
        )

    print(
        f"Generated {output_path}"
    )

for candidate in csv_candidates:

    if not candidate["email"]:
        continue

    email = candidate["email"].lower()

    if email in matched_emails:
        continue

    profile = {

        "full_name":
        candidate["full_name"],

        "primary_email":
        candidate["email"],

        "primary_phone":
        candidate["phone"],

        "skills": [],

        "experience": None,

        "overall_confidence": 0.75
    }

    filename = (
        email.split("@")[0]
    )

    output_path = os.path.join(
        output_folder,
        filename + ".json"
    )

    with open(
        output_path,
        "w"
    ) as f:

        json.dump(
            profile,
            f,
            indent=4
        )

    print(
        f"CSV-only candidate: {email}"
    )

print(
    "\nAll candidate profiles generated successfully."
)