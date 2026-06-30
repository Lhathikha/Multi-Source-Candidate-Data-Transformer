from src.normalizer import (
    normalize_email,
    normalize_phone
)


def match_candidate(
        csv_candidates,
        resume_data):

    resume_email = normalize_email(
        resume_data["email"]
    )

    resume_phone = normalize_phone(
        resume_data["phone"]
    )

    resume_name = (
        resume_data["name"]
        .lower()
        if resume_data["name"]
        else None
    )

    # Priority 1: Email

    for candidate in csv_candidates:

        candidate_email = normalize_email(
            candidate["email"]
        )

        if (
            resume_email
            and
            candidate_email
            and
            candidate_email == resume_email
        ):
            return candidate

    # Priority 2: Phone

    for candidate in csv_candidates:

        candidate_phone = normalize_phone(
            candidate["phone"]
        )

        if (
            resume_phone
            and
            candidate_phone
            and
            candidate_phone == resume_phone
        ):
            return candidate

    # Priority 3: Name

    for candidate in csv_candidates:

        if not candidate["full_name"]:
            continue

        candidate_name = (
            candidate["full_name"]
            .lower()
        )

        if (
            resume_name
            and
            candidate_name == resume_name
        ):
            return candidate

    return None