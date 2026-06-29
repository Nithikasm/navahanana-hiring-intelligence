# src/ranking/behavioral_score.py

from datetime import datetime, timezone


def compute_behavioral_score(candidate):
    """
    Returns score in [0, 1].

    Measures candidate availability and responsiveness.
    """

    score = 0.5  # neutral starting point

    signals = candidate.get("redrob_signals", {})

    # Recruiter response rate
    response_rate = signals.get("recruiter_response_rate", -1)

    if response_rate != -1:
        score += 0.3 * response_rate

    # Interview completion rate
    completion_rate = signals.get("interview_completion_rate", -1)

    if completion_rate != -1:
        score += 0.2 * completion_rate

    # Recent activity
    last_active = candidate.get("last_active_date")

    if last_active:
        try:
            last_active_dt = datetime.fromisoformat(
                last_active.replace("Z", "+00:00")
            )

            days_inactive = (
                datetime.now(timezone.utc) - last_active_dt
            ).days

            if days_inactive <= 30:
                score += 0.2
            elif days_inactive > 180:
                score -= 0.2

        except Exception:
            pass

    return max(0.0, min(score, 1.0))