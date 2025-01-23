# JSONPath Normalized Test Suite

A suite of tests for _normalized paths_, the string representation of a node's location as defined by [section 2.7 of RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535#name-normalized-paths).

This is inspired by the [JSONPath Compliance Test Suite](https://github.com/jsonpath-standard/jsonpath-compliance-test-suite) and we've copied/adapted many test cases and the JSON schema therein. See the CTS license [here](https://github.com/jsonpath-standard/jsonpath-compliance-test-suite/blob/main/LICENSE).

## Canonical paths

`canonical_paths.json` contains test cases for serializing a "compiled" JSONPath query back to a string. The canonical representation of a compiled query is not a normalized path, is not necessarily a singular query and is not specified by RFC 9535.

For our purposes, a canonical path is one that:

- uses bracket notation rather than shorthand selectors
- uses single quotes rather than double quotes
- includes the default step of `1` in slice selectors
- excludes enclosing parentheses in filter selectors. `?<expression>` rather than `?(<expression>)`
- minimizes parentheses in logical expressions
- follows escaping rules defined in [section 2.7 of RFC 9535](https://datatracker.ietf.org/doc/html/rfc9535#name-normalized-paths).
- uses exactly one space character either side of logical and comparison expressions
- uses exactly one space character after a comma
