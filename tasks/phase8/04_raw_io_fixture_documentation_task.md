# Task 04: Raw I/O Fixture Documentation

Status: done

## Goal

Document raw fixture formats and how they map into normalized SignalTwin frames.

## Domain Boundary

This task owns docs only.

## Files

- Create `docs/raw-io-fixtures.md`
- Modify `docs/device-io-assumptions.md` if fixture names or required fields change
- Modify `tests/test_raw_fixture_contracts.py`

## TDD Checklist

- [x] RED: write `test_raw_io_fixture_doc_mentions_all_fixture_files`.
- [x] Verify RED:

```bash
pytest tests/test_raw_fixture_contracts.py::test_raw_io_fixture_doc_mentions_all_fixture_files -v
```

Expected failure:

- missing docs

- [x] GREEN: document every raw fixture file and normalized target frame.
- [x] Verify GREEN:

```bash
pytest tests/test_raw_fixture_contracts.py::test_raw_io_fixture_doc_mentions_all_fixture_files -v
```

Expected:

- test passes

## Done Criteria

- Docs explain assumed devices and replacement options.
- Docs state fixture contracts are development contracts, not final hardware requirements.
- Raw fixture docs remain consistent with `docs/device-io-assumptions.md`.

## Regression Verification

Run the Phase 8 regression command from `tasks/phase8/phase_test.md` before marking this task `done`.

## Commit Checkpoint

```bash
git add docs/raw-io-fixtures.md tests/test_raw_fixture_contracts.py
git commit -m "docs: add raw io fixture contracts"
```
