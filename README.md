
# 🔬 PubMed Fetcher Thanush

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Published-TestPyPI-yellow)
![Built with Poetry](https://img.shields.io/badge/Built%20With-Poetry-cyan)

> 🎯 A command-line tool to fetch **PubMed research papers** containing at least one **non-academic author** (like those from pharma or biotech industries), and save them to a neat **CSV file**.  
> 🚀 Built with 💙 by [**Thanush Shetty**](mailto:thanushshetty7@gmail.com)



## 🧠 Features

✨ Simple CLI tool with the power of:
- 🔎 Accepts flexible PubMed query syntax
- 🧬 Uses PubMed's **Entrez API**
- 🏢 Identifies **non-academic authors** via smart affiliation heuristics
- 📩 Extracts **corresponding author emails**
- 🗂️ Outputs results as CSV
- 🛠️ CLI with `--debug`, `--file`, and `--max` options
- 📦 Ready to install via **TestPyPI**

---

## 🚀 Quick Start

```bash
get-papers-list "covid vaccine" --max 50 --debug --file result.csv
````

✅ Command-line Options:

| Flag        | Description                                    |
| ----------- | ---------------------------------------------- |
| query       | PubMed search query (required)                 |
| -f, --file  | Save output to this CSV file (default: stdout) |
| -d, --debug | Show debug info                                |
| -m, --max   | Max papers to fetch (default: 100)             |
| -h, --help  | Show help info                                 |

📥 Sample Output

```
Saved to result.csv:
PubmedID    Title              Date        Non-academic Authors    Company       Email
12345678    COVID Drug Trial  2024-03-05  John Smith              Pfizer Inc    jsmith@pfizer.com
```

---

## ⚙️ Installation

🔹 **Option 1: From TestPyPI**

```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-fetcher-thanush
```

🔹 **Option 2: Clone & Use with Poetry**

```bash
git clone https://github.com/your-username/pubmed-fetcher-thanush.git
cd pubmed-fetcher-thanush
poetry install
poetry run get-papers-list "ai in healthcare" --max 30 --file result.csv --debug
```

---

## 📂 Project Structure

```
pubmed_fetcher_thanush/
├── __init__.py
├── fetcher.py       # Handles PubMed API calls
├── filter.py        # Extracts, filters, and parses XML
├── utils.py         # Helper functions for author classification
├── main.py          # CLI entry point
pyproject.toml       # Poetry config
README.md            # You're reading it
```

---

## 🔗 Resources

* 📚 [PubMed API Docs](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
* 📦 [TestPyPI Project Page](https://test.pypi.org/project/pubmed-fetcher-thanush/)
* 📘 [PubMed Query Syntax Guide](https://pubmed.ncbi.nlm.nih.gov/help/)

---

## 🧪 How We Identify Non-Academic Authors

We use keyword-based heuristics to detect authors not affiliated with academic institutions:

✅ **Non-Academic Keywords:**
`"inc", "ltd", "company", "pharma", "therapeutics", "biotech", "corporation"`

🚫 **Academic Keywords (excluded):**
`"university", "college", "institute", "school", "hospital", "lab"`

---

## 🧪 Development & Testing

Want to test the project locally?

```bash
poetry build
poetry run get-papers-list "lung cancer" -f output.csv -d
```

To publish to TestPyPI:

```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi pypi-***************
poetry publish -r test-pypi
```

---

## ⚙️ Built With

* `requests`
* `pandas`
* `argparse`
* `xml.etree.ElementTree`
* `Poetry`

---

## 🤖 AI & ChatGPT Usage

This project was carefully structured and refined with the help of ChatGPT for:

* 📦 Clean packaging
* 🧩 Modular code structure
* 🛠️ CLI argument setup
* 📄 README formatting

---

## 🙌 Author

**Thanush Shetty**
📧 [thanushshetty7@gmail.com](mailto:thanushshetty7@gmail.com)

## 📄 License

Licensed under the MIT License. See `LICENSE` for full details.

