import re


def extract_email(text):

    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    return emails


def extract_phone(text):

    phones = re.findall(
        r'(\+91[\s-]?)?\d{10}',
        text
    )

    result = []

    for phone in phones:

        if isinstance(phone, tuple):
            number = ''.join(phone)

            if number:
                result.append(number)

        elif phone:
            result.append(phone)

    return result


def extract_experience(text):

    match = re.search(
        r'(\d+)\s+year',
        text.lower()
    )

    if match:
        return int(match.group(1))

    return None


def extract_skills(text):

    skills_db = [
        "Python",
        "Java",
        "SQL",
        "AWS",
        "Power BI",
        "Excel",
        "Machine Learning"
    ]

    found = []

    lower_text = text.lower()

    for skill in skills_db:

        if skill.lower() in lower_text:
            found.append(skill)

    return found
def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            return line

    return None