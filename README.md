# React Project Analysis Tool

This project is a modular Python tool designed to analyze React projects. It scans directories to find React component files, analyzes their usage across the project, and identifies associated style files (e.g., `.module.scss`, `.module.css`). The results are saved as a formatted text file on the user's desktop.

## Features

- **React Component File Detection**: Scans directories to find all React component files (`.js`, `.jsx`, `.ts`, `.tsx`).
- **Usage Analysis**: Counts how many times each component is imported or used across the project.
- **Style File Detection**: Identifies associated `.module.scss` and `.module.css` files for each component.
- **Results Export**: Saves the results as a structured array in a text file on the user's desktop.
- **Modular Design**: The tool is organized into separate modules for better maintainability and scalability.

## Project Structure

```
react_project_analysis/
├── main.py                     # Entry point for the application
├── utils/
│   ├── file_scanner.py         # Functions for scanning React files
│   ├── usage_analysis.py       # Functions for analyzing component usage
│   ├── style_analysis.py       # Functions for detecting style files
│   └── file_saver.py           # Functions for saving results to a file
└── README.md                   # Documentation for the project
```

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/react-project-analysis-tool.git
   cd react-project-analysis-tool
   ```

2. Ensure you have Python 3.7 or higher installed. You can check your Python version with:

   ```bash
   python --version
   ```

3. (Optional) Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

4. Install dependencies (if any are required in future).

## Usage

1. Run the tool by executing the `main.py` file:

   ```bash
   python main.py
   ```

2. Enter the path to your React project when prompted. Example:

   ```
   Enter the path to your React project: /path/to/your/project
   ```

3. The tool will:
   - Scan the provided directory for React component files.
   - Analyze usage of each component in other files.
   - Identify style files associated with the components.
   - Save the results as a text file on your desktop (e.g., `react_component_files_array.txt`).

4. Check your desktop for the output file.

## Modules

### 1. `file_scanner.py`
Contains the `get_react_component_files` function, which:
- Recursively scans a directory to identify React component files.
- Skips unnecessary directories such as `node_modules`, `stories`, etc.

### 2. `usage_analysis.py`
Contains the `find_component_usages` function, which:
- Analyzes how many times each component is imported across the project.
- Uses regular expressions to detect imports.

### 3. `style_analysis.py`
Contains the `find_styles_for_components` function, which:
- Identifies `.module.scss` and `.module.css` files in the same directory as the components.

### 4. `file_saver.py`
Contains the `save_to_desktop` function, which:
- Saves the list of React components and style files to a text file on the user's desktop.

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Thanks to all open-source contributors and the Python community for making this project possible.

