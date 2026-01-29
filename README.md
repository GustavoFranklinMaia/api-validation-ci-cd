# Rick and Morty API Tests (Pytest + CI)

![CI](../../actions/workflows/ci.yml/badge.svg)

API test automation project using **Pytest**, with **GitHub Actions CI** running on every PR/push.

## Tech Stack
- Python 3.11
- Pytest
- Requests
- GitHub Actions
- JUnit report + Coverage report

## How to Run Locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
pytest -v
