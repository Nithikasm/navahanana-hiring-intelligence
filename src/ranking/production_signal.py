# src/ranking/production_signal.py

PRODUCTION_KEYWORDS = {
    "deployed",
    "deployment",
    "production",
    "prod",
    "shipped",
    "maintained",
    "scaled",
    "monitoring",
    "monitored",
    "pipeline",
    "serving",
    "latency",
    "uptime",
    "a/b testing",
    "ab testing",
    "real-time",
    "real time",
    "millions of users",
    "index refresh",
    "drift",
    "regression testing"
}


def compute_production_signal_score(candidate_text):
    """
    Returns score in [0,1]
    Measures evidence of production ML/search systems.
    """

    text = candidate_text.lower()

    matches = sum(
        keyword in text
        for keyword in PRODUCTION_KEYWORDS
    )

    return matches / len(PRODUCTION_KEYWORDS)