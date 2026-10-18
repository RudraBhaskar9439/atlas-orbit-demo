# Orbit — Atlas company-brain demo

**Clearly labeled synthetic demonstration.** This small Python repository demonstrates Atlas's company brain: who did a change, who reviewed it, who owns the affected service, and which decision depends on current evidence. People and review history in `COMPANY_CONTEXT.md` are fictional records; real GitHub author metadata and test results remain real.

The main product is [Atlas Engineering Workspace](https://github.com/RudraBhaskar9439/atlas-engineering-workspace).

## Run

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The initial five tests pass. The intentionally uncovered half-cent billing case is reported in the sample issue. Fix it in Atlas by adding the regression test and changing only the relevant rounding behavior.

## Company-brain walkthrough

1. Read the sample team handoff in `COMPANY_CONTEXT.md`, or import `company-records.json` through Atlas's structured record importer.
2. Ask who authored the auth change, who reviewed it, who owns auth, and what Noah is assigned to do next. Open the cited source record for each claim.
3. Inspect the ownership and decision paths in the graph.
4. Continue the same investigation with a second connected model. Keep the recorded owners, evidence, and unresolved questions.
5. Demonstrate a failed authentication verification causing the launch decision to need review while the unrelated billing decision stays unchanged.
6. Optionally investigate the public billing issue, review the proposed patch, run real isolated tests, and explicitly approve a draft PR in this repository.

This repository is owned by the recording account, so the PR destination can be this repository itself; no fork is required. CI runs Python tests only and does not push container images to another organization's registry. Draft publication and merging are separate actions.

For the shortest company-brain video, Atlas's existing Orbit demo workspace already includes the core ownership, authored-change, review, and launch scenario. Keep the synthetic-data label visible and use this public repository for the optional code-to-PR scene.
