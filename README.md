# validated-api-payload-inspector
CLI that loads mock API payloads, validates them with pydantic, reports useful errors, and includes at least five tests.

## Assignment

1. Pydantic model for a mock lead payload
2. CLI that takes a JSON file path and validates it
3. Readable errors showing field path and message, all errors in one run
4. Graceful handling of a missing file or malformed JSON
5. Exit code 0 for valid, non-zero for invalid
6. Sample payloads: one valid, several invalid
7. At least five pytest tests

### Definition of done
1. Same input gives the same output every time
2. Error messages are readable
3. All tests pass
4. No secrets or caches committed

### Extra credit
1. Nested model with error paths like `contacts.1.email`
2. Batch mode with a summary for a whole folder
3. `--json` output flag
4. `--strict` flag to turn off type coercion
5. Cross-field validator
6. GitHub Actions running pytest and ruff