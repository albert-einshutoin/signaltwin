# Contributing

Thanks for taking the time to improve SignalTwin. This project is still an MVP, so contributions should keep the hardware-free contract clear and testable.

## Development Setup

```bash
python -m pip install -e '.[test,dev]'
pytest
```

If optional dev tools are unavailable in your environment, run the test suite at minimum and mention which tools were skipped.

## Contribution Scope

Good first contribution areas:

- documentation fixes
- new scenario fixtures
- adapter contract tests
- clearer validation errors
- risk model documentation and examples

Before adding real-device integrations, update the relevant adapter contract and keep the existing fixture-based path working.

## Pull Request Checklist

- Keep the risk engine independent from hardware-specific adapter modules.
- Add or update tests for behavior changes.
- Update `README.md`, `README.ja.md`, or `docs/README.md` when public workflows change.
- Keep generated runtime outputs out of commits unless they are named example contracts.
- Run `pytest` before opening a pull request.

## Commit Style

Use short, conventional messages when practical:

```txt
docs: clarify adapter contract
test: cover invalid bms fixture
feat: add thermal adapter validation
fix: preserve typed scenario payload
```
