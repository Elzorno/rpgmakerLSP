from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

def run_validate():
    script = ROOT / "atlas-tools" / "validator" / "atlas_validate.py"
    return subprocess.call([sys.executable, str(script)])

def main():
    if len(sys.argv) < 2:
        print("Usage: python atlas-tools/cli/atlas.py <command>")
        print("Commands: validate")
        return 1

    command = sys.argv[1]

    if command == "validate":
        return run_validate()

    print(f"Unknown command: {command}")
    return 1

if __name__ == "__main__":
    sys.exit(main())