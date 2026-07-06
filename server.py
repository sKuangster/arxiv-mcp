from mcp.server.fastmcp import FastMCP
from arxiv_client import search_papers, get_paper_by_id

mcp = FastMCP("arxiv-digest")

@mcp.tool()
def get(id: int) -> str:


@mcp.tool()
def search_arxiv(query: str, max_results: int = 5) -> list:
    """Search arXiv papers by keyword."""
    ...

mcp.run(transport="stdio")