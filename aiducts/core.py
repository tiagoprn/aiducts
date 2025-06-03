from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import os
import sys
import traceback

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

from integrations.github import fetch_pr_changes


class AIductsMCPServer:
    def __init__(self):
        load_dotenv()

        self.mcp = FastMCP("aiducts_mcp_server")
        print("MCP Server initialized", file=sys.stderr)

        self._register_tools()

        self.data_folder = os.getenv('DATA_FOLDER')
        if self.data_folder:
            data_path = Path(self.data_folder)
            self.markdown_path = data_path / "markdown"
            self.markdown_path.mkdir(parents=True, exist_ok=True)
        else:
            raise Exception("Warning: DATA_FOLDER environment variable not set", file=sys.stderr)

    def _register_tools(self):
        """Register MCP tools."""

        @self.mcp.tool()
        async def fetch_pr(repo_owner: str, repo_name: str, pr_number: int) -> Dict[str, Any]:
            """Fetch changes from a GitHub pull request."""
            print(f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}", file=sys.stderr)
            try:
                pr_info = fetch_pr_changes(repo_owner, repo_name, pr_number)
                if pr_info is None:
                    print("No changes returned from fetch_pr_changes", file=sys.stderr)
                    return {}
                print("Successfully fetched PR information", file=sys.stderr)
                return pr_info
            except Exception as e:
                print(f"Error fetching PR: {str(e)}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return {}

        @self.mcp.tool()
        async def create_markdown_document(title: str, content: str) -> str:
            """Create a Markdown file"""
            print(f"Creating Notion page: {title}", file=sys.stderr)
            try:
                timestamp = datetime.now().strftime('%Y%m%d.%H%M%S.%f')
                path = f'{self.markdown_path}/{timestamp}.md'
                with open(path, 'w') as output_file:
                    output_file.writelines([title, '', content])

                print(f"Markdown file '{path}'  created successfully with title='{title}'!", file=sys.stderr)
                return f"Markdown file '{path}'  created successfully with title='{title}'!"
            except Exception as e:
                error_msg = f"Error creating Notion page: {str(e)}"
                print(error_msg, file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return error_msg

    def run(self):
        """Start the MCP server."""
        try:
            print("Running AIducts MCP Server...", file=sys.stderr)
            self.mcp.run(transport="stdio")
        except Exception as e:
            print(f"Fatal Error in MCP Server: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    server = AIductsMCPServer()
    server.run()
