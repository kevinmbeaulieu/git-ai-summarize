import os
import subprocess
from typing import Optional, Tuple


def verify_git_repo():
    """Verify current directory is a git repository."""
    if not os.path.exists('.git'):
        raise RuntimeError("Not a git repository")


def get_git_diff(args) -> Optional[str]:
    """Get the diff between commits with optional arguments."""
    try:
        cmd = ['git', 'diff'] + args
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None


def get_current_head() -> Optional[str]:
    """Get the current HEAD commit hash."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def git_pull() -> Tuple[bool, str]:
    """Perform git pull and return success status and output."""
    try:
        result = subprocess.run(
            ['git', 'pull'],
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"Error during git pull:\n{e.stderr}"


async def stream_response(stream):
    """Stream the response from LLM."""
    async for chunk in stream:
        print(chunk, end="", flush=True)
    print()
