from src.canonical import create_profile
from src.confidence import calculate_confidence


def merge(candidate, resume):

    profile = create_profile()

    profile["full_name"] = (
        resume["name"]
        if resume["name"]
        else candidate["full_name"]
    )

    if candidate["email"]:
        profile["emails"].append({
            "value": candidate["email"],
            "sources": ["csv"]
        })

    if resume["email"]:

        exists = False

        for email in profile["emails"]:

            if email["value"] == resume["email"]:
                email["sources"].append(
                    "resume"
                )
                exists = True

        if not exists:

            profile["emails"].append({
                "value": resume["email"],
                "sources": ["resume"]
            })

    if candidate["phone"]:
        profile["phones"].append({
            "value": candidate["phone"],
            "sources": ["csv"]
        })

    if resume["phone"]:

        exists = False

        for phone in profile["phones"]:

            if phone["value"] == resume["phone"]:
                phone["sources"].append(
                    "resume"
                )
                exists = True

        if not exists:

            profile["phones"].append({
                "value": resume["phone"],
                "sources": ["resume"]
            })

    for skill in resume["skills"]:

        profile["skills"].append({
            "name": skill,
            "confidence": 0.9,
            "sources": ["resume"]
        })

    profile["years_experience"] = (
        resume["experience"]
    )

    confidence_values = []

    for email in profile["emails"]:
        confidence_values.append(
            calculate_confidence(
                email["sources"]
            )
        )

    if confidence_values:

        profile["overall_confidence"] = (
            sum(confidence_values)
            /
            len(confidence_values)
        )

    return profile