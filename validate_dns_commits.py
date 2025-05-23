import subprocess
import os
import sys
import dns.zone
import dns.exception

# Configurable zone directory
ZONE_DIR = "zones"

def get_staged_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True
    )
    return [f for f in result.stdout.strip().split('\n') if f.endswith('.zone')]

def validate_zone_file(path):
    try:
        zone = dns.zone.from_file(path, os.path.basename(path))
        print(f"[OK] {path}: Zone file is valid")
        return True
    except dns.exception.DNSException as e:
        print(f"[ERROR] {path}: DNS validation failed - {e}")
        return False
    except Exception as e:
        print(f"[ERROR] {path}: General validation failure - {e}")
        return False

def main():
    print("Validating DNS zone files...")
    files = get_staged_files()
    if not files:
        print("No DNS zone files staged for commit.")
        return 0

    failed = False
    for f in files:
        if not validate_zone_file(f):
            failed = True

    if failed:
        print("Commit aborted due to invalid DNS zone files.")
        return 1
    else:
        print("All zone files valid. Proceeding with commit.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
