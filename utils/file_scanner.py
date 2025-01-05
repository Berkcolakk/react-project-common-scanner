import os

def get_react_component_files(directory):
    """Get all React component files (.js, .jsx, .ts, .tsx) in the project."""
    component_files = []
    for root, _, files in os.walk(directory):
        # Skip unnecessary directories
        if any(skip in root for skip in ["node_modules", "stories", "types", "consts", "functions"]):
            continue
        for file in files:
            if file.endswith((".js", ".jsx", ".ts", ".tsx")):
                component_files.append(os.path.join(root, file))
    return component_files
