import os

def save_to_desktop(output_list):
    """Save the list to a text file on the desktop."""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "react_component_files_array.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("[\n")
        f.write(",\n".join(f'"{item}"' for item in output_list))
        f.write("\n]")
    print(f"Results saved to: {output_file}")
