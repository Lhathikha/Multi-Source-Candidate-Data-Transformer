import pandas as pd


NAME_FIELDS = [
    "name",
    "candidate_name",
    "full_name"
]

EMAIL_FIELDS = [
    "email",
    "mail",
    "email_id"
]

PHONE_FIELDS = [
    "phone",
    "mobile",
    "contact"
]


def get_value(row, fields):
    for column in row.index:
        if column.lower().strip() in fields:
            value = row[column]

            if pd.isna(value):
                return None

            return str(value)

    return None


def parse_csv(path):
    df = pd.read_csv(path)

    candidates = []

    for _, row in df.iterrows():

        candidate = {
            "full_name": get_value(row, NAME_FIELDS),
            "email": get_value(row, EMAIL_FIELDS),
            "phone": get_value(row, PHONE_FIELDS)
        }

        candidates.append(candidate)

    return candidates