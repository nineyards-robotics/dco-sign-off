# dco-sign-off

A [pre-commit](https://pre-commit.com/) hook that automatically adds a [DCO](https://developercertificate.org/) Signed-off-by` line to your commit messages using your Git committer identity.

## Usage

Add to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/nineyards-robotics/dco-sign-off
  rev: v1.0.0
  hooks:
  - id: dco-sign-off
```

Then install the hook:

```bash
pre-commit install --hook-type prepare-commit-msg
```

The hook runs at the `prepare-commit-msg` stage, so it needs the `--hook-type` flag since pre-commit defaults to the `pre-commit` stage.

## How it works

When you make a commit, the hook checks if a `Signed-off-by:` line is already present. If not, it appends one using the name and email from your Git config (equivalent to `git commit -s`).

## License

See [LICENSE](LICENSE).
