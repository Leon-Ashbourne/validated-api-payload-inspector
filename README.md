# validated-api-payload-inspector
CLI that loads mock API payloads, validates them with pydantic, reports useful errors, and includes at least five tests.

# Assignment

Pydantic model for a mock lead payload
CLI that takes a JSON file path and validates it
Readable errors showing field path and message, all errors in one run
Graceful handling of a missing file or malformed JSON
Exit code 0 for valid, non-zero for invalid
Sample payloads: one valid, several invalid
At least five pytest tests

# Definition of done
Same input gives the same output every time
Error messages are readable
All tests pass
No secrets or caches committed
Public post published

# Extra credit
Nested model with error paths like `contacts.1.email`
Batch mode with a summary for a whole folder
`--json` output flag
`--strict` flag to turn off type coercion
Cross-field validator
GitHub Actions running pytest and ruff