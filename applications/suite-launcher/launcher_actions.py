from pathlib import Path


def launch_module(module):
    print(f"\n[LAUNCH]")
    print(f"Launching: {module['name']}")
    print(f"Location: {module['location']}")


def show_documentation(module):
    print(f"\n[DOCUMENTATION]")

    for document in module.get("documentation", []):
        print(f" - {document}")


def show_workflows(module):
    print(f"\n[WORKFLOWS]")

    for workflow in module.get("workflows", []):
        print(f" - {workflow}")


def show_module_directory(module):
    print(f"\n[DIRECTORY]")
    print(module["location"])


def module_actions_menu(module):
    while True:

        print("\n==============================")
        print(module["name"])
        print("==============================")

        print("1. Launch Module")
        print("2. Show Documentation")
        print("3. Show Workflows")
        print("4. Show Directory")
        print("0. Back")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            launch_module(module)

        elif choice == "2":
            show_documentation(module)

        elif choice == "3":
            show_workflows(module)

        elif choice == "4":
            show_module_directory(module)

        elif choice == "0":
            break

        else:
            print("Invalid selection.")
