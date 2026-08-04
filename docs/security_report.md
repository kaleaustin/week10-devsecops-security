# Security Report

## Executive Summary

This project demonstrates how DevSecOps tools identify and remediate security issues before deployment.

## Security Tools

- Bandit
- pip-audit
- Gitleaks

## Bandit Findings

Detected:

- MD5 hashing
- os.system()
- subprocess(shell=True)
- eval()
- pickle.loads()
- Hardcoded password
- Weak random

Remediation:

- SHA256
- secrets module
- Removed eval()
- Removed shell=True
- Removed os.system()
- Removed pickle.loads()

## Dependency Findings

Old Flask and Requests versions contained vulnerabilities.

Updated to latest secure releases.

## Secret Findings

Hardcoded credentials detected.

Moved to environment variables.

## Pipeline Verification

Bandit Passed

pip-audit Passed

Gitleaks Passed

## Lessons Learned

Security should be integrated into CI/CD before deployment.
