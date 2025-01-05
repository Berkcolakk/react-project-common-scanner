import os
import re
from collections import Counter

def find_component_usages(component_files, directory):
    """Find how many times each component file is used in the project."""
    component_usage = Counter()
    component_names = {os.path.basename(file).rsplit('.', 1)[0]: file for file in component_files}

    for root, _, files in os.walk(directory):
        if any(skip in root for skip in ["node_modules", "stories", "types", "consts", "functions"]):
            continue
        for file in files:
            if file.endswith((".js", ".jsx", ".ts", ".tsx")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        for component_name in component_names.keys():
                            import_regex = rf"import\s+(.*\b{re.escape(component_name)}\b.*)"
                            if re.search(import_regex, content):
                                component_usage[component_name] += 1
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    return component_usage
