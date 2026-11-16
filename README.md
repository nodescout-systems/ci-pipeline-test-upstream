# ci-pipeline-test-upstream

A small Python package that stands in for an upstream open-source project. It exists only to test manual forks and the automatic upstream update in [nodescout-systems/ci-config](https://github.com/nodescout-systems/ci-config). Nothing depends on it.

Its changes are made deliberately, to simulate what real upstream projects do: releases, changes that conflict with a fork's customizations, changes that break tests, and new automation.

It carries its own automation on purpose, as many upstream projects do:

- `.github/workflows/upstream-ci.yml` runs on pushes, pull requests, a weekly schedule, and by hand. It only prints which repository and ref it ran in, so that a run in a fork's repository shows up.
- `.github/dependabot.yml` asks Dependabot for weekly updates of the Python dependencies.

## Using it

```bash
uv run ci-pipeline-test-upstream Ada
```

prints `Hello, Ada.`
