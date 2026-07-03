from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

def run_validate():
    script = ROOT / "atlas-tools" / "validator" / "atlas_validate.py"
    return subprocess.call([sys.executable, str(script)])

def run_next():
    script = ROOT / "atlas-tools" / "generators" / "workorder_next.py"
    return subprocess.call([sys.executable, str(script)])

def main():
    if len(sys.argv) < 2:
        print("Usage: python atlas-tools/cli/atlas.py <command>")
        print("Commands: validate, next")
        return 1

    command = sys.argv[1]

    if command == "validate":
        return run_validate()

    if command == "next":
        return run_next()

    print(f"Unknown command: {command}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
