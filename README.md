![Static Badge](https://img.shields.io/badge/python-3.9-%233776AB?logo=python)
![Static Badge](https://img.shields.io/badge/scrapy-2.5.1-%2360A839?logo=scrapy)
![Static Badge](https://img.shields.io/badge/pytest-6.2.5-%230A9EDC?logo=pytest)


# scrapy_parser_pep

This is a project that utilizes Scrapy to parse PEP (Python Enhancement Proposals) documents.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)

## Installation
### basic
1. Clone the repository:
```bash
git clone https://github.com/alisher-nil/scrapy_parser_pep.git
```
2. Navigate to the project directory:
```bash
cd scrapy_parser_pep
```
3. Create virtual environment
```bash
python -m venv .venv
```
4. Update pip
```bash
python -m pip install --upgrade pip
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
### uv
The project can be initialized with [uv](https://docs.astral.sh/uv/).
```bash
# after moving to a project's directory
uv sync
```
## Usage

To run the PEP parser, use the following command from the project directory:

```bash
scrapy crawl pep
# or with uv
uv run scrapy crawl pep
```

The result should be two csv files:
1. pep_< date >.csv containing a list with numbers, names and current statuses of all peps.
2. status_summary_< date >.csv containing a list of statuses and their counts among all the peps in descending order with a total.

## Author
Please feel free to contact me with any questions or feedback:

- Email: alisher.nil@gmail.com
- GitHub: [alisher-nil](https://github.com/alisher-nil/)