"""
Inside the aiducts folder (where "core.py" is located),
run this script as a python module:

python -m manual_tests.github_integration
"""
from pprint import pprint

from integrations.github import fetch_pr_changes

pr_data = fetch_pr_changes('tiagoprn', 'aiducts', 1)
pprint(pr_data)
