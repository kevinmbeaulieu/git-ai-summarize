import os
import subprocess
from typing import Optional, Tuple


def verify_git_repo():
    """Verify current directory is a git repository."""
    if not os.path.exists('.git'):
        raise RuntimeError("Not a git repository")


def get_git_diff(from_commit: str, to_commit: str) -> Optional[str]:
    """Get the diff between two commits."""
    try:
        result = subprocess.run(
            ['git', 'diff', from_commit, to_commit],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None


def verify_commit_exists(commit: str) -> bool:
    """Verify if a commit exists in the repository."""
    try:
        subprocess.run(
            ['git', 'rev-parse', '--verify', commit],
            capture_output=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def parse_commit_range(commit_arg: str) -> Tuple[str, str]:
    """Parse commit argument into from_commit and to_commit."""
    if '..' in commit_arg:
        from_commit, to_commit = commit_arg.split('..')
        if not from_commit or not to_commit:
            raise ValueError(
                "Invalid commit range format. Use 'commit1..commit2'")
        return from_commit.strip(), to_commit.strip()
    return commit_arg.strip(), 'HEAD'


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
