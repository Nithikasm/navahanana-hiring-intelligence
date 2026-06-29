# src/ranking/final_feature_extractor.py

from src.preprocessing.candidate_text_builder import build_candidate_text

from src.features.technical_fit import (
    compute_core_skill_score
)

from src.features.relevance_signals import (
    compute_relevance_signal_score
)

from src.ranking.production_signal import (
    compute_production_signal_score
)

from src.ranking.pre_llm_experience import (
    compute_pre_llm_experience_score
)

from src.ranking.behavioral_score import (
    compute_behavioral_score
)

from src.ranking.disqualifier_detector import (
    compute_disqualification_risk
)


def extract_ranking_features(candidate):
    """
    Extract all ranking features for a candidate.

    Returns:
        dict
    """

    candidate_text = build_candidate_text(candidate)

    features = {
        "core_skill_score":
            compute_core_skill_score(candidate),

        "relevance_score":
            compute_relevance_signal_score(candidate_text),

        "production_score":
            compute_production_signal_score(candidate_text),

        "pre_llm_score":
            compute_pre_llm_experience_score(candidate),

        "behavioral_score":
            compute_behavioral_score(candidate),

        "disqualification_risk":
            compute_disqualification_risk(candidate)
    }

    return features