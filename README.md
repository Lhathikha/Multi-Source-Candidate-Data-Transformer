# Multi-Source Candidate Data Transformer


---

# Problem Statement

Candidate information is often distributed across multiple sources such as recruiter CSV files and candidate resumes. The same candidate may appear in different sources with missing fields, duplicate information, inconsistent formats, or conflicting details. Because of this, generating one reliable candidate profile becomes difficult and time-consuming.

The objective of this project is to design a simple and explainable transformation system that combines multiple sources and generates one trustworthy candidate profile without manual verification.

---

# Proposed Solution

This project proposes a multi-source candidate transformation pipeline that combines recruiter CSV data and candidate resumes to generate a single canonical candidate profile.

The system automatically:

- Detects input sources.
- Extracts candidate information.
- Standardizes extracted values.
- Matches candidate records.
- Resolves conflicting information.
- Assigns confidence scores.
- Generates a unified output profile.

The final profile remains reliable even when information is incomplete, inconsistent, or available from only one source.

---

# Supported Inputs

### Structured Source

- Recruiter CSV

### Unstructured Sources

- PDF Resume
- DOCX Resume

### Matching Priority

1. Email
2. Phone Number
3. Name

### Source Priority

Resume → CSV

Resume information is treated as the latest candidate-provided information.

---

# Features

- Supports multiple candidates in a single CSV file.
- Supports multiple PDF resumes.
- Supports multiple DOCX resumes.
- Automatically detects input file types.
- Extracts candidate information from resumes.
- Normalizes email addresses and phone numbers.
- Matches candidates using multiple attributes.
- Resolves conflicting information using source priority.
- Assigns confidence scores based on source agreement.
- Generates canonical candidate profiles.
- Handles incomplete information gracefully.
- Produces consistent JSON outputs.

---

# Project Structure

```text
Eightfold-Assignment/
│
├── input/
│   ├── candidates.csv
│   └── resumes/
│       ├── john.pdf
│       ├── ram.docx
│       └── priya.pdf
│
├── output/
│
├── config/
│   └── default_config.json
│
├── src/
│   ├── csv_parser.py
│   ├── pdf_parser.py
│   ├── docx_parser.py
│   ├── extractor.py
│   ├── matcher.py
│   ├── merger.py
│   ├── normalizer.py
│   ├── projector.py
│   ├── validator.py
│   └── detector.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Transformation Pipeline

```text
CSV + PDF/DOCX
        ↓
Detect
        ↓
Extract
        ↓
Normalize
        ↓
Match
        ↓
Merge
        ↓
Confidence
        ↓
Output
```

---

# Pipeline Description

### Detect

Identifies whether the input source is CSV, PDF, or DOCX.

### Extract

Extracts:
- Name
- Email
- Phone Number
- Skills
- Experience

### Normalize

Converts different formats into standardized values.

Example:

```text
JOHN@GMAIL.COM
↓
john@gmail.com
```

### Match

Matches candidates using:

1. Email
2. Phone Number
3. Name

### Merge

Combines information from multiple sources.

Resume → CSV

### Confidence

Higher confidence is assigned when multiple sources agree.

### Output

Generates a canonical candidate profile in JSON format.

---

# Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Default Execution

The system automatically uses:

```text
input/candidates.csv
input/resumes/
output/
```

Run:

```bash
python main.py
```

---

## Custom CLI Execution

Provide custom input and output locations:

```bash
python main.py <csv_file> <resume_folder> <output_folder>
```

Example:

```bash
python main.py company.csv company_resumes result
```

---

# Output

The system generates a separate JSON profile for each candidate.

Example:

```json
{
    "full_name": "John Doe",
    "primary_email": "john@gmail.com",
    "primary_phone": "+919876543210",
    "overall_confidence": 0.95
}
```

---

# Edge Cases Handled

| Edge Case | Handling |
|----------|-----------|
| Multiple CSV candidates | Each row is processed independently |
| Resume-only candidates | Profile generated using resume data |
| CSV-only candidates | Available CSV information retained |
| Missing email or phone | Remaining information is processed |
| Different CSV columns | Alias mapping identifies equivalent fields |
| Duplicate information | Source priority resolves conflicts |
| Multiple resumes | Each resume is processed separately |
| Unsupported files | Invalid files are skipped safely |

---

# Assumptions

- Resumes are text-based PDF or DOCX files.
- At least one identifying field is available.
- Resume information represents the latest candidate information.
- Candidate matching is performed using available attributes.

---

# Limitations

- OCR-based extraction is not supported.
- Image-based resumes are not supported.
- Highly graphical resumes may produce partial extraction.
- Complex resume layouts may reduce extraction accuracy.
- Text-based PDF and DOCX resumes are recommended.

---

# Future Improvements

- OCR support for scanned resumes.
- NLP-based information extraction.
- Layout-aware resume parsing.
- Advanced confidence scoring.
- Web-based user interface.

---

# Demo Video

The complete implementation, workflow explanation, and output demonstration are available in the demo video.

```
Demo Video Link
```

---

# Author

**Lhathikha V**  
Final Year B.E. Computer Science and Engineering  
KPR Institute of Engineering and Technology