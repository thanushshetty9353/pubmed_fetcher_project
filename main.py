# main.py
import sys
import csv
from fetcher import fetch_pubmed_ids, fetch_paper_details
from filter import extract_paper_info

def save_to_csv(papers, filename="output.csv"):
    if not papers:
        print("No non-academic papers found.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=papers[0].keys())
        writer.writeheader()
        for row in papers:
            writer.writerow(row)
    print(f"Saved {len(papers)} papers to {filename}")

def main():
    if len(sys.argv) < 2:
        print("Please provide a search query.")
        print("Usage: python main.py 'cancer vaccine'")
        return

    query = sys.argv[1]
    print(f"Searching PubMed for: {query}")
    ids = fetch_pubmed_ids(query)
    xml_data = fetch_paper_details(ids)
    papers = extract_paper_info(xml_data)
    save_to_csv(papers)

if __name__ == "__main__":
    main()
