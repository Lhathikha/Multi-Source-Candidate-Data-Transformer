from src.merger import merge

candidate = {
    "full_name": "John Doe",
    "email": "john@gmail.com",
    "phone": "9876543210"
}

resume = {
    "name": "John Doe",
    "email": "john@gmail.com",
    "phone": "9876543210",
    "skills": [
        "Python",
        "Java"
    ],
    "experience": 2
}

profile = merge(
    candidate,
    resume
)

print(profile)