#BINDIYA SUDARSUN 22MIC0040  
#results.md:

# StudentProfile RPC Validation Results

## Test Cases

| Case | Input | Output |
|-----|------|--------|
| Valid Profile | Correct types | Average calculated |
| Invalid ID | String instead of int | TypeError |
| Invalid Grades | Non-integer value | TypeError |

## Observation

Type validation in the marshalling layer prevents malformed RPC requests from being processed on the server.
