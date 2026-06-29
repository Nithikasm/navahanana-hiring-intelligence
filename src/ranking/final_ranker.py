# src/ranking/final_ranker.py

from src.ranking.final_feature_extractor import (
    extract_ranking_features
)


def compute_final_score(candidate):
    """
    Compute final candidate ranking score.

    Returns:
        float in [0, 1]
    """

    features = extract_ranking_features(candidate)

    score = (
        0.30 * features["core_skill_score"] +
        0.20 * features["relevance_score"] +
        0.20 * features["production_score"] +
        0.15 * features["pre_llm_score"] +
        0.15 * features["behavioral_score"]
    )

    # Penalize suspicious candidates
    score *= (1 - 0.5 * features["disqualification_risk"])

    return round(score, 4)