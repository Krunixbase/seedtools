from pathlib import Path

def execute_entrypoint(module):
    """
    Prepare module execution.
    """

    selected = select_runnable_entrypoint(module)

    if not selected:
        print("Status: NO VALID ENTRYPOINT")
        return

    print("\n[EXECUTE ENTRYPOINT]")
    print(f"Selected: {selected['name']}")
    print(f"Path: {selected['path']}")
    print("Status: EXECUTABLE")

    run_entrypoint(module)

def run_entrypoint(module):
    """
    Simulate module execution.
    """

    selected = select_runnable_entrypoint(module)

    if not selected:
        print("Status: NOT RUNNABLE")
        return

    print("\n[RUN ENTRYPOINT]")
    print(f"Selected: {selected['name']}")
    print(f"Path: {selected['path']}")
    print("Status: RUNNING")
    print("Status: COMPLETED")

    launch_real_process(selected)

def launch_real_process(selected):

    if not selected:
        print("Process: FAILED")
        return

    print("\n[REAL EXECUTION]")
    print(f"Selected: {selected['name']}")
    print(f"Path: {selected['path']}")

    if not Path(selected["path"]).exists():
        print("Process: FAILED")
        return

    print("Process: PREPARED")

def detect_entrypoints(module):
    """
    Return module entrypoints.
    """

    return module.get("entrypoints", {})

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

def validate_entrypoints(module):
    """
    Validate module entrypoints.
    """

    module_dir = resolve_module_directory(module)

    entrypoints = detect_entrypoints(module)

    results = {}

    for name, entrypoint in entrypoints.items():

        entrypoint_path = module_dir / entrypoint

        results[name] = {
            "path": str(entrypoint_path),
            "exists": entrypoint_path.exists()
        }

    return results

def select_runnable_entrypoint(module):
    """
    Select first runnable entrypoint.
    """

    entrypoints = validate_entrypoints(module)

    for name, info in entrypoints.items():

        if info["exists"]:

            return {
                "name": name,
                "path": info["path"],
                "exists": True
            }

    return None

def launch_module(module):

    print("\n[RUNNER]")

    validation = validate_module(module)

    print(f"Module: {module['name']}")
    print(f"Location: {validation['directory']}")

    if not validation["exists"]:
        print("Status: NOT FOUND")
        return

    print("Status: READY")

    entrypoints = validate_entrypoints(module)

    if not entrypoints:
        print("Entrypoints: NOT DEFINED")
        return

    print("\nEntrypoints:")

    for name, info in entrypoints.items():

        status = "FOUND" if info["exists"] else "MISSING"

        print(f" - {name}: {status}")

    execute_entrypoint(module)

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


