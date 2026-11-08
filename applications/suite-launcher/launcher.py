import json
from pathlib import Path

from launcher_actions import module_actions_menu

REGISTRY_FILE = Path(__file__).parent / "registry.json"


def load_registry():
    with REGISTRY_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def display_modules(registry):
    print("\nSeedTools Suite Launcher")
    print("=" * 30)

    modules = registry.get("modules", [])

    for index, module in enumerate(modules, start=1):
        print(f"{index}. {module['name']}")

    print("0. Exit")


def display_module_details(module):
    print("\n" + "=" * 40)
    print(f"Name: {module['name']}")
    print(f"Version: {module['version']}")
    print(f"Category: {module['category']}")
    print(f"Status: {module['status']}")
    print(f"Location: {module['location']}")
    print(f"Description: {module['description']}")

    print("\nLaunch Methods:")
    for method in module.get("launch_methods", []):
        print(f" - {method}")

    print("\nWorkflows:")
    for workflow in module.get("workflows", []):
        print(f" - {workflow}")

    print("\nDocumentation:")
    for document in module.get("documentation", []):
        print(f" - {document}")

    print("=" * 40)


def launcher_loop():
    registry = load_registry()

    while True:
        display_modules(registry)

        choice = input("\nSelect module: ").strip()

        if choice == "0":
            print("Exiting Launcher...")
            break

        if not choice.isdigit():
            print("Invalid selection.")
            continue

        index = int(choice) - 1

        modules = registry.get("modules", [])

        if index < 0 or index >= len(modules):
            print("Invalid selection.")
            continue

        module = modules[index]

        display_module_details(module)

        module_actions_menu(module)

def main():
    launcher_loop()


if __name__ == "__main__":
    main()
