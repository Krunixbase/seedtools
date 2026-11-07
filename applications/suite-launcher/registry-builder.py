import json
from pathlib import Path


APPLICATIONS_DIR = Path(__file__).resolve().parents[1]
OUTPUT_REGISTRY = Path(__file__).parent / "registry.json"


def load_module_metadata(module_file: Path) -> dict:
    with module_file.open("r", encoding="utf-8") as f:
        return json.load(f)


def discover_modules() -> list:
    modules = []

    for directory in APPLICATIONS_DIR.iterdir():
        if not directory.is_dir():
            continue

        module_json = directory / "module.json"

        if not module_json.exists():
            continue

        try:
            metadata = load_module_metadata(module_json)
            modules.append(metadata)

        except Exception as exc:
            print(f"[ERROR] {module_json}: {exc}")

    return modules


def build_registry() -> dict:
    return {
        "version": "1.0.0",
        "registry_name": "SeedTools Suite Registry",
        "generated_by": "registry-builder.py",
        "modules": discover_modules()
    }


def save_registry(registry: dict) -> None:
    with OUTPUT_REGISTRY.open("w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def main() -> None:
    registry = build_registry()

    save_registry(registry)

    print("[OK] Registry generated")
    print(f"[OK] Modules discovered: {len(registry['modules'])}")
    print(f"[OK] Registry written: {OUTPUT_REGISTRY}")


if __name__ == "__main__":
    main()
