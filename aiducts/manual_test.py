from pprint import pprint
re

from integrations.github import fetch_pr_changes

pr_data = fetch_pr_changes('tiagoprn', 'aiducts', 1)
pprint(pr_data)
