"""
Inside the aiducts folder (where "core.py" is located),
run this script as a python module:

python -m manual_tests.mcp_functions
"""
import json
import sys


def check_function_create_markdown_document():
    request = {
       "jsonrpc": "2.0",
       "method": "create_markdown_document",
       "params": {
           "title": "# Test Document",
           "content": "This is a test document created via MCP."
       }
    }

    print(json.dumps(request))
    sys.stdout.flush()

    response = json.loads(input())
    print(f"Response: {response}")


def check_function_fetch_pr():
    request = {
       "jsonrpc": "2.0",
       "method": "fetch_pr",
       "params": {
           "repo_owner": "tiagoprn",
           "repo_name": "aiducts",
           "pr_number": 1
       }
    }

    print(json.dumps(request))
    sys.stdout.flush()

    response = json.loads(input())
    print(f"Response: {response}")


def main():
    # check_function_fetch_pr()
    check_function_create_markdown_document()


if __name__ == '__main__':
    main()
