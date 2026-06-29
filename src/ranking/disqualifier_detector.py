CONSULTING_COMPANIES = {
    "tcs",
    "infosys",
    "wipro",
    "accenture",
    "cognizant",
    "capgemini",
    "hcl",
    "tech mahindra"
}

NON_TECH_TITLES = {
    "marketing manager",
    "sales manager",
    "business development manager",
    "account manager",
    "hr manager",
    "recruiter"
}


def detect_consulting_only(candidate):

    career = candidate.get("career_history", [])

    companies = []

    for role in career:
        company = role.get("company", "").lower().strip()

        if company:
            companies.append(company)

    if not companies:
        return False

    return all(
        any(c in company for c in CONSULTING_COMPANIES)
        for company in companies
    )


def detect_non_technical_ai_profile(candidate):

    title = (
        candidate.get("profile", {})
        .get("current_title", "")
        .lower()
    )

    return title in NON_TECH_TITLES


def compute_disqualification_risk(candidate):
    """
    Returns risk score in [0,1]
    0 -> safe
    1 -> highly suspicious
    """

    risk = 0.0

    if detect_consulting_only(candidate):
        risk += 0.4

    if detect_non_technical_ai_profile(candidate):
        risk += 0.6

    return min(risk, 1.0)