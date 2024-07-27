# Simple Port Scanner

A Simple Port Scanner built with Python that scans a specified IP address for open ports within a given range.

## Features

- Scans a specified IP address for open ports within a given range.
- Quickly identifies open ports to help in network security assessments.
- Easy to use with command-line inputs.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### Step 1: Install Python

1. Download Python from the official website: [Python Downloads](https://www.python.org/downloads/).
2. Run the installer and ensure you check the option to add Python to your PATH.

### Step 2: Install an IDE (Visual Studio Code or PyCharm)

#### Visual Studio Code

1. Download and install Visual Studio Code from [VS Code Downloads](https://code.visualstudio.com/Download).
2. Install the Python extension for Visual Studio Code:
   - Open Visual Studio Code.
   - Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window.
   - Search for "Python" and install the official Python extension.

#### PyCharm

1. Download and install PyCharm from [PyCharm Downloads](https://www.jetbrains.com/pycharm/download/).
2. Open PyCharm and configure the Python interpreter:
   - Go to `File > Settings > Project: <project name> > Project Interpreter`.
   - Click the gear icon and select `Add`.
   - Choose `System Interpreter` and select the Python installation path.

### Step 3: Set Up the Project

1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/yourusername/simple-port-scanner.git
   cd simple-port-scanner

## Usage
Open the project in your preferred IDE (VS Code or PyCharm).

## Visual Studio Code
Open Visual Studio Code.

Open the folder containing your project (File > Open Folder).

Open a new terminal (Terminal > New Terminal).

Run the script using the following command:
```python
python main.py
```

## PyCharm
Open PyCharm.
Open the project (File > Open and select the project folder).
Right-click on main.py and select Run 'main'.
## Running the Script
When you run the script, you will be prompted to enter the IP address, starting port, and ending port. The script will then scan the specified range and output the open ports.

Example output:
```python
Enter the IP address to scan: 192.168.1.1
Enter the starting port (1-65535): 1
Enter the ending port (1-65535): 1024
Scanning 192.168.1.1 from port 1 to 1024...
Open ports on 192.168.1.1: [22, 80, 443]
```

## Contributing
If you have suggestions or improvements, feel free to create an issue or submit a pull request. Contributions are always welcome!

## License
This project is licensed under the MIT License.

This README provides clear instructions for setting up the project, running the port scanner, and understanding its output. It also includes a code example and details about contributing to the project.


