# utils.py
def is_non_academic(affiliation: str) -> bool:
    """
    Return True if the affiliation is non-academic.
    Looks for pharma/biotech keywords and filters out academic ones.
    """
    keywords = ["inc", "ltd", "company", "pharma", "therapeutics", "biotech", "corporation"]
    academic_words = ["university", "institute", "college", "school", "hospital", "lab"]
    aff = affiliation.lower()
    return any(k in aff for k in keywords) and not any(a in aff for a in academic_words)
