def calculate_fraud_score(aadhaar_valid: bool, pan_valid: bool) -> int:
    score = 0

    if not aadhaar_valid:
        score += 50

    if not pan_valid:
        score += 50

    return score


def is_fraud(score: int) -> bool:
    return score >= 50
