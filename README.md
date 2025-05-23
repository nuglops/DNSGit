# DNSGit

Here's a Python script to validate commits to a Git-based DNS package repository. This script assumes:

You're working with DNS zone files or configuration files in a Git repo.

You want to validate DNS records syntax or integrity before allowing a commit.

The validation is done as a Git pre-commit hook or via CI.

We'll use dnspython for basic DNS validation.

Features:
Scans changed files in a commit.

Validates DNS record syntax using dnspython.

Can be expanded to check for duplicates, TTL ranges, or zone formatting.
