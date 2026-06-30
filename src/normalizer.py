import re


def normalize_email(email):

    if email:
        return email.lower().strip()

    return None


def normalize_phone(phone):

    if not phone:
        return None

    digits = re.sub(
        r'\D',
        '',
        phone
    )

    if len(digits) == 10:
        return "+91" + digits

    if len(digits) == 12:
        return "+" + digits

    return phone


def normalize_skills(skills):

    normalized = []

    for skill in skills:
        normalized.append(
            skill.title()
        )

    return list(set(normalized))