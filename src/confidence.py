def calculate_confidence(sources):

    count = len(set(sources))

    if count >= 2:
        return 1.0

    return 0.8