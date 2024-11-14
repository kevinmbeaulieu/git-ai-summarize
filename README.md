# Git AI Summarize

A command-line tool for summarizing changes in Git repositories using AI.

## Installation

```bash
pip install git-ai-summarize
```

## Requirements

- Python 3.8 or higher
- An API key for Anthropic (or your preferred LLM)

## Setup

Set an environment variable with your LLM API key. To use the default Anthropic model, use:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Add this to your shell profile to make it permanent.

## Commands

### Summarize changes between commits

Provide a commit hash or a range of commits to get a summary of the changes.

```bash
# Compare with HEAD
git summarize <commit-hash>

# Compare any two commits
git summarize <commit1>..<commit2>
```

### Pull and summarize changes

Pass the `--pull` flag to pull changes from the remote and summarize the changes since the last pull.

```bash
git summarize --pull
```

## Using alternative LLM providers/models

You can pass the `--provider` and `--model` argument to use a different LLM provider/model. The default provider is `anthropic`, and the default model is `claude-3-5-sonnet-latest`. To get a list of all supported providers, run:

```bash
git summarize --list-providers
```

To get a list of all supported models for a provider, see the LLM providers' documentation.

Depending on the provider, you may need to set additional environment variables with that provider's API key (e.g., `ANTHROPIC_API_KEY` for Anthropic/Claude, `OPENAI_API_KEY` for OpenAI/GPT, etc.).

To change your default provider/model, you can set the `GIT_SUMMARIZE_PROVIDER` and `GIT_SUMMARIZE_MODEL` environment variables.

If you would like to use a model by a provider that is not currently supported by this package, feel free to submit an Issue with the name of the model/provider and we can look into it. If it is supported by LangChain, we can most likely add it.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

GNU GPLv3 License
