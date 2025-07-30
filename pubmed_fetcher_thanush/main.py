import argparse
import csv
from typing import List, Dict
from pubmed_fetcher_thanush.fetcher import fetch_pubmed_ids, fetch_paper_details
from pubmed_fetcher_thanush.filter import extract_paper_info

def save_to_csv(papers: List[Dict], filename: str = "output.csv") -> None:
    """Save filtered paper data to a CSV file."""
    if not papers:
        print("No non-academic papers found.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=papers[0].keys())
        writer.writeheader()
        for row in papers:
            writer.writerow(row)
    print(f"Saved {len(papers)} papers to {filename}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with at least one non-academic author.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Filename to save CSV output", default="output.csv")
    parser.add_argument("-d", "--debug", help="Print debug information", action="store_true")
    parser.add_argument("-m", "--max", help="Maximum number of papers to fetch", type=int, default=100)

    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Query: {args.query}")
        print(f"[DEBUG] Output file: {args.file}")
        print(f"[DEBUG] Max results: {args.max}")

    ids = fetch_pubmed_ids(args.query, args.max)

    if args.debug:
        print(f"[DEBUG] Found {len(ids)} PubMed IDs")

    xml_data = fetch_paper_details(ids)
    papers = extract_paper_info(xml_data)
    save_to_csv(papers, args.file)

if __name__ == "__main__":
    main()
