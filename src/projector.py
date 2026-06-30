def get_value(profile, source):

    if source == "emails[0]":

        if profile["emails"]:
            return profile["emails"][0]["value"]

        return None

    if source == "phones[0]":

        if profile["phones"]:
            return profile["phones"][0]["value"]

        return None

    return profile.get(source)


def project(profile, config):

    output = {}

    for field in config["fields"]:

        if "from" in field:

            value = get_value(
                profile,
                field["from"]
            )

        else:

            value = profile.get(
                field["path"]
            )

        output[field["path"]] = value

    if config["include_confidence"]:

        output["overall_confidence"] = (
            profile["overall_confidence"]
        )

    if config["include_provenance"]:

        output["provenance"] = (
            profile["provenance"]
        )

    return output