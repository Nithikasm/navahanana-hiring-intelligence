# src/preprocessing/role_classifier.py

TECH_KEYWORDS = {
    "software engineer",
    "backend engineer",
    "frontend engineer",
    "full stack developer",
    "data engineer",
    "data scientist",
    "ml engineer",
    "machine learning engineer",
    "ai engineer",
    "devops engineer",
    "cloud engineer",
    "analytics engineer",
    "qa engineer",
    "sre",
    "site reliability engineer",
    "java developer",
    ".net developer",
    "python developer",
    "mobile developer",
    "android developer",
    "ios developer",
    "architect",
    "platform engineer",
    "engineering manager",
    "ai specialist",
    "ai research engineer",
    "recommendation systems engineer",
    "search engineer",
    "relevance engineer",
    "retrieval engineer",
    "nlp engineer",
    "research engineer",
    "machine learning scientist",
    "data analyst"
}

NON_TECH_KEYWORDS = {
    "sales",
    "marketing",
    "accountant",
    "hr",
    "human resources",
    "recruiter",
    "content writer",
    "graphic designer",
    "customer support",
    "operations manager",
    "business development",
    "relationship manager",
    "mechanical engineer",
    "civil engineer",
    "project manager",
    "construction engineer",
    "electrical engineer",
    "automobile engineer",
    "manufacturing engineer"
}


def classify_role(title: str) -> str:
    """
    Returns:
        'technical'
        'non_technical'
        'unknown'
    """

    if not title:
        return "unknown"

    title = title.lower().strip()

    for keyword in TECH_KEYWORDS:
        if keyword in title:
            return "technical"

    for keyword in NON_TECH_KEYWORDS:
        if keyword in title:
            return "non_technical"

    return "unknown"
if __name__ == "__main__":

    test_titles = [
        "Software Engineer",
        "Marketing Manager",
        "ML Engineer",
        "HR Manager",
        "Senior Data Engineer",
        "Business Analyst"
    ]

    for title in test_titles:
        print(f"{title} --> {classify_role(title)}")
