# Security Policy

SignalTwin is a hardware-free MVP and should not be treated as a deployed building monitoring system.

## Supported Versions

Only the current `main` branch is maintained.

## Reporting a Vulnerability

Please report security issues privately through GitHub Security Advisories for this repository when available. If that is not available, open a minimal issue that does not include exploit details and ask for a private contact path.

Include:

- affected commit or version
- reproduction steps
- impact assessment
- whether untrusted input, generated reports, or local files are involved

## Security Boundaries

Current trusted scope:

- local CLI execution
- repository fixtures and examples
- schema-validated adapter outputs
- deterministic report generation

Out of scope for the current MVP:

- production API deployment
- real sensor ingestion
- authentication and authorization
- tenant isolation
- remote execution sandboxing
- field safety decisions based only on SignalTwin output

Security-sensitive changes should include tests for invalid input, path handling, and schema validation failure modes.
