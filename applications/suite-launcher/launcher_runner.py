from pathlib import Path


def resolve_module_directory(module):
    """
    Resolve module directory from metadata.
    """

    location = module.get("location")

    if not location:
        raise ValueError("Missing module location.")

    root_dir = Path(__file__).resolve().parents[2]

    return root_dir / location


def validate_module(module):
    """
    Validate basic module structure.
    """

    module_dir = resolve_module_directory(module)

    return {
        "exists": module_dir.exists(),
        "directory": str(module_dir)
    }


def launch_module(module):
    """
    MVP launcher action.

    Current version validates module metadata
    and module directory before execution.
    """

    print("\n[RUNNER]")

    validation = validate_module(module)

    print(f"Module: {module['name']}")
    print(f"Location: {validation['directory']}")

    if validation["exists"]:
        print("Status: READY")
    else:
        print("Status: NOT FOUND")


def show_module_info(module):
    """
    Display runtime information.
    """

    print("\n[MODULE INFO]")

    print(f"Name: {module['name']}")
    print(f"Version: {module['version']}")
    print(f"Category: {module['category']}")
    print(f"Status: {module['status']}")

    print("\nLaunch Methods:")

    for method in module.get("launch_methods", []):
        print(f" - {method}")
