# src/features/technical_fit.py

CORE_AI_SKILLS = {
    "nlp",
    "information retrieval",
    "semantic search",
    "hybrid search",
    "embeddings",
    "vector database",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "faiss",
    "elasticsearch",
    "bm25",
    "ranking",
    "recommendation systems",
    "recommendation systems engineer",
    "retrieval",
    "rag",
    "llm",
    "fine-tuning llms",
    "lora"
}


def compute_core_skill_score(candidate: dict) -> float:
    """
    Returns a score between 0 and 1
    based on presence of core AI/retrieval skills.
    """

    skills = candidate.get("skills", [])

    candidate_skills = {
        skill.get("name", "").lower()
        for skill in skills
        if isinstance(skill, dict)
    }

    matches = candidate_skills.intersection(CORE_AI_SKILLS)

    return len(matches) / len(CORE_AI_SKILLS)