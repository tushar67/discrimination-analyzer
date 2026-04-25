bias_terms = {
    "Age Bias":["young"],
    "Gender Bias":["salesman","waitress","barman"],
    "Nationality Bias":["native italian","italian only"],
    "Appearance Bias":["good looking"]
}

def analyze_bias(text):
    issues = []
    lower = text.lower()

    for category, words in bias_terms.items():
        for word in words:
            if word in lower:
                issues.append({
                    "category": category,
                    "term": word
                })

    score = max(100 - len(issues)*20, 0)

    return {
        "score": score,
        "issues": issues
    }