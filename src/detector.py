import os


def detect_resume_type(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return "pdf"

    elif extension == ".docx":
        return "docx"

    else:
        return None