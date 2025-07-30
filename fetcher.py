# fetcher.py
import requests

def fetch_pubmed_ids(query):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 20
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['esearchresult']['idlist']

def fetch_paper_details(id_list):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(id_list),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    return response.text  # XML data (we will process this)
