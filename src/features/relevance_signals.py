# src/features/relevance_signals.py

HIGH_VALUE_KEYWORDS = {
    "ndcg",
    "mrr",
    "recall@k",
    "precision@k",
    "learning to rank",
    "ltr",
    "bm25",
    "hybrid retrieval",
    "information retrieval",
    "vector search",
    "semantic search",
    "ranking",
    "relevance",
    "retrieval",
    "recommendation systems",
    "behavioral signals",
}


def compute_relevance_signal_score(candidate_text: str) -> float:
    """
    Measures evidence of search/ranking/retrieval expertise.
    Returns score in [0, 1].
    """

    text = candidate_text.lower()

    matches = sum(
        1 for keyword in HIGH_VALUE_KEYWORDS
        if keyword in text
    )

    return matches / len(HIGH_VALUE_KEYWORDS)