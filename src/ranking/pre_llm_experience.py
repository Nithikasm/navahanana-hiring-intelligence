# src/ranking/pre_llm_experience.py

from datetime import datetime

PRE_LLM_KEYWORDS = {
    "search",
    "retrieval",
    "ranking",
    "recommendation",
    "recommendation system",
    "information retrieval",
    "recommender",
    "personalization",
    "semantic search"
}


def compute_pre_llm_experience_score(candidate):
    """
    Returns score in [0,1].

    Rewards candidates who worked on
    retrieval/ranking/recommendation before 2022.
    """

    career = candidate.get("career_history", [])

    relevant_roles = 0

    for role in career:

        start_date = role.get("start_date", "")

        try:
            year = datetime.fromisoformat(start_date).year
        except:
            continue

        if year >= 2022:
            continue

        text = (
            role.get("title", "") + " " +
            role.get("description", "")
        ).lower()

        if any(keyword in text for keyword in PRE_LLM_KEYWORDS):
            relevant_roles += 1

    return min(relevant_roles / 3, 1.0)