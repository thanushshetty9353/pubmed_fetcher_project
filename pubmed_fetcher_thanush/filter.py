import xml.etree.ElementTree as ET
from typing import List, Dict
from .utils import is_non_academic


def extract_paper_info(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        email = "Not available"
        non_acad_authors = []
        companies = []

        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//AffiliationInfo/Affiliation")
            if affiliation and is_non_academic(affiliation):
                name = (author.findtext("LastName") or "") + ", " + (author.findtext("ForeName") or "")
                non_acad_authors.append(name)
                companies.append(affiliation)
            if affiliation and "@" in affiliation and email == "Not available":
                email = affiliation.split()[-1]

        if non_acad_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email
            })

    return papers
