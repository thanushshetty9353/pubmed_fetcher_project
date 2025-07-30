import requests
from typing import List

def fetch_pubmed_ids(query: str, max_results: int = 100) -> List[str]:
    """Fetch PubMed IDs based on the search query."""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data['esearchresult']['idlist']
    except Exception as e:
        print(f"[ERROR] Failed to fetch PubMed IDs: {e}")
        return []

def fetch_paper_details(id_list: List[str]) -> str:
    """Fetch paper details (XML) using a list of PubMed IDs."""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "xml"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[ERROR] Failed to fetch paper details: {e}")
        return ""
