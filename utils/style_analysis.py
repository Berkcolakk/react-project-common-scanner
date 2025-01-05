import os

def find_styles_for_components(component_files):
    """Find .module.scss or .module.css files related to the components."""
    component_styles = set()
    for component_file in component_files:
        component_dir = os.path.dirname(component_file)
        try:
            styles = [
                os.path.basename(style_file)
                for style_file in os.listdir(component_dir)
                if style_file.endswith((".module.scss", ".module.css"))
            ]
            component_styles.update(styles)
        except Exception as e:
            print(f"Error reading styles in {component_dir}: {e}")

    return component_styles
