# CRUD APP - README

## Description
CRUD APP is a simple command-line application for managing client data using basic CRUD (Create, Read, Update, Delete) operations. The application allows users to create new client records, read and search existing records, update client information, and delete client records.

## Installation
1. Clone this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Set up a virtual environment (optional but recommended).
4. Install the required dependencies by running: `pip install -r requirements.txt`

## Usage
1. Navigate to the project directory.
2. Run the main.py file to start the application: `python main.py`
3. Follow the on-screen instructions to interact with the application.
4. The main menu will present four options:
   - **1**: Create a new client record.
   - **2**: Read and search existing client records.
   - **3**: Update client information.
   - **4**: Delete a client record.
   - **exit**: End the session and exit the application.

## Project Structure
The project contains the following files and folders:

- `app/`: Main application folder. *at this moment is empty
- `documents/`: Folder for storing client records in a CSV file.
   - `Registers.csv`: CSV file for storing client information.
- `test/`: Folder for testing code and testing-related files.
   - `__pycache__/`: Compiled Python files (automatically generated).
   - `create_new_client.py`: Test code for creating a new client.
   - `registers.py`: Module containing functions to read and search client records.
   - `seconds_screens.py`: Module containing functions for displaying secondary screens.
   - `testing_tools.py`: Module containing testing-related functions.
- `Utils/`: Folder containing utility functions and modules.
  - `__pycache__/`: Compiled Python files (automatically generated).
  - `__init__.py`: Empty file indicating the folder is a Python package.
  - `create_registers.py`: Module for creating new client records.
  - `delete_registers.py`: Module for deleting client records (empty implementation).
  - `read_registers.py`: Module for reading and searching client records.
  - `screens.py`: Module containing functions for displaying main screens.
  - `seconds_screens.py`: Module containing functions for displaying secondary screens.
  - `tools.py`: Module containing various utility functions.
  - `update_register.py`: Module for updating client records (empty implementation).
- `venv/`: Virtual environment folder (automatically created if using virtual environment).
- `main.py`: Main entry point of the application.
- `README.md`: This file - contains project information and instructions.

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request with your proposed changes. Any contributions are welcome!


## Contact
For any questions or inquiries, please contact me.
