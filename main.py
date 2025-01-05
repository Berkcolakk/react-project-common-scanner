import os
from utils.file_scanner import get_react_component_files
from utils.usage_analysis import find_component_usages
from utils.style_analysis import find_styles_for_components
from utils.file_saver import save_to_desktop

def collect_files_with_usages_and_styles(directory):
    """Collect all React component and style files, including usage analysis."""
    component_files = get_react_component_files(directory)
    component_usage = find_component_usages(component_files, directory)

    used_components = [
        os.path.basename(file_path)
        for file_name, file_path in {
            os.path.basename(file).rsplit('.', 1)[0]: file for file in component_files
        }.items()
        if component_usage[file_name] > 0
    ]

    style_files = find_styles_for_components(component_files)
    all_files = used_components + list(style_files)
    return all_files

def main():
    project_path = input("Enter the path to your React project: ").strip()
    if not os.path.isdir(project_path):
        print("Invalid directory. Please provide a valid path.")
        return

    print("Scanning for React component and style files...")
    result = collect_files_with_usages_and_styles(project_path)

    print(result)
    save_to_desktop(result)

if __name__ == "__main__":
    main()
