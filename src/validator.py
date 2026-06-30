def validate(profile):

    errors = []

    if not profile["full_name"]:

        errors.append(
            "Missing name"
        )

    if not profile["emails"]:

        errors.append(
            "Missing email"
        )

    return errors