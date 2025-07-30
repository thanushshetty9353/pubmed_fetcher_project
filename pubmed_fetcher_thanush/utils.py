def is_non_academic(affiliation: str) -> bool:
    """Check if an affiliation is non-academic (like a company)."""
    keywords = ["inc", "ltd", "company", "pharma", "therapeutics", "biotech", "corporation"]
    academic_words = ["university", "institute", "college", "school", "hospital", "lab"]

    aff = affiliation.lower()
    return any(k in aff for k in keywords) and not any(a in aff for a in academic_words)
