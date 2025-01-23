"""Validate test suites against their schemas."""

import json

from jsonschema import validate

NORMALIZED_PATHS = "normalized_paths.json"
NORMALIZED_PATHS_SCHEMA = "normalized_paths.schema.json"

CANONICAL_PATHS = "canonical_paths.json"
CANONICAL_PATHS_SCHEMA = "canonical_paths.schema.json"


def _validate(file_path: str, schema_file_path: str) -> None:
    with open(file_path, encoding="utf-8") as fd:
        tests = json.load(fd)

    with open(schema_file_path, encoding="utf-8") as fd:
        schema = json.load(fd)

    validate(instance=tests, schema=schema)


if __name__ == "__main__":
    _validate(NORMALIZED_PATHS, NORMALIZED_PATHS_SCHEMA)
    _validate(CANONICAL_PATHS, CANONICAL_PATHS_SCHEMA)
