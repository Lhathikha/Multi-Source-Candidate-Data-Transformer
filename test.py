from src.pdf_parser import parse_pdf
from src.extractor import *

text = parse_pdf(
    "input/resumes/john.pdf"
)

print(extract_name(text))

print(extract_email(text))

print(extract_phone(text))

print(extract_skills(text))

print(extract_experience(text))