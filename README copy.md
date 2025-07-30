# 🔬 PubMed Fetcher Thanush

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Published-TestPyPI-yellow)
![Built with Poetry](https://img.shields.io/badge/Built%20With-Poetry-cyan)

> A command-line tool to fetch **PubMed research papers** containing at least one **non-academic author**, particularly from **pharma or biotech companies**, and export the data to CSV.  
> Built with 💙 by **Thanush Shetty**.

---

## 🧠 Features

- 🔎 Accepts flexible PubMed query syntax
- 🧬 Fetches data using PubMed's **Entrez API**
- 🏢 Identifies **non-academic authors** using affiliation heuristics
- 📩 Extracts **corresponding author emails**
- 🗂️ Outputs results as CSV or console preview
- 🛠 CLI powered by `argparse` with `--debug`, `--file`, and `--max`
- 📦 Distributed via [TestPyPI](https://test.pypi.org/project/pubmed-fetcher-thanush)

---

## 🖥️ CLI Usage

```bash
get-papers-list "covid vaccine" --debug --file result.csv
```

### ✅ Command-line Options:

| Flag            | Description                                  |
|-----------------|----------------------------------------------|
| `query`         | Your PubMed search query (required)          |
| `-f, --file`    | CSV file to save results (default: output.csv) |
| `-d, --debug`   | Print debug information                      |
| `-m, --max`     | Maximum number of papers to fetch (default: 100) |
| `-h, --help`    | Show usage help                              |

---

## 📥 Example Output

Saved to `result.csv`:
| PubmedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|----------|-------|------------------|--------------------------|--------------------------|-----------------------------|
| 12345678 | COVID Drug Trial | 2024 | John Smith | Pfizer Inc | jsmith@pfizer.com |

---

## ⚙️ Installation

### 🔹 Option 1: From TestPyPI (Recommended for Reviewers)

```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-fetcher-thanush
```

### 🔹 Option 2: Clone and Use Locally with Poetry

```bash
git clone https://github.com/your-username/pubmed-fetcher-thanush.git
cd pubmed-fetcher-thanush
poetry install
poetry run get-papers-list "diabetes vaccine" -f diabetes.csv
```

---

## 📦 Project Structure

```
pubmed_fetcher_thanush/
├── __init__.py
├── fetcher.py       # API fetch logic
├── filter.py        # Paper parsing and filtering
├── utils.py         # Heuristics for non-academic detection
├── main.py          # CLI entry point
pyproject.toml       # Poetry config
README.md            # You’re reading this
```

---

## 🔗 Resources

- 📚 [PubMed API (Entrez)](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- 🐍 [Python 3.9+](https://www.python.org/downloads/)
- 📦 [Poetry](https://python-poetry.org/)
- 📁 [TestPyPI Project](https://test.pypi.org/project/pubmed-fetcher-thanush/)
- 📊 [PubMed Search Syntax Guide](https://pubmed.ncbi.nlm.nih.gov/help/)

---

## 💡 How We Identify Non-Academic Authors

A heuristic checks for keywords in affiliations:
- Academic: `"university", "college", "institute", "school", "hospital", "lab"`
- Non-Academic: `"inc", "ltd", "company", "pharma", "therapeutics", "biotech", "corporation"`

---

## 🧪 Development & Testing

Want to test locally?

```bash
poetry build
poetry run get-papers-list "lung cancer" -f output.csv -d
```

To publish to TestPyPI:

```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi pypi-*************
poetry publish -r test-pypi
```

---

## 🧠 Tools & Libraries Used

- [`requests`](https://docs.python-requests.org/en/latest/)
- [`pandas`](https://pandas.pydata.org/)
- [`argparse`](https://docs.python.org/3/library/argparse.html)
- [`Poetry`](https://python-poetry.org/)
- [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html)

---

## 🤖 LLM Assistance

This project was partially planned and refined using [ChatGPT](https://chat.openai.com/), following best practices in code modularity, CLI design, and packaging.

---

## 🙌 Acknowledgments

Thanks to the problem reviewers for evaluating this package. Built with ❤️ and Python.

---

## 📄 License

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for details.