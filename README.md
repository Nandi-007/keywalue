# Keyvalue Project

The Keyvalue project is a key-value store implementation built on Windows OS using Windows Subsystem for Linux (WSL)
with WSL 2.

## Prerequisites

Before running the project, make sure you have the following prerequisites:

- Windows operating system (Windows 10 or higher)
- WSL 2 installed and configured
- PyCharm (or any preferred Python IDE) for development

## WSL 2 Configuration

To configure WSL 2, follow these steps:

1. Install WSL 2 by following the official Microsoft
   documentation: [WSL 2 Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
2. Set WSL 2 as the default WSL version by running the following command in PowerShell with administrator privileges:

  ```
  wsl --set-default-version 2
  ```

## Setup and Installation

1. Clone the repository to your local machine.
2. Install the required Python packages by running the following command:

  ```
  pip install -r requirements.txt
  ```

## Usage

To run the project in PyCharm, follow these steps:

1. Open the project in PyCharm.
2. Set up the additional arguments for pytest in the Run Configuration:

- Open the Run Configuration dialog in PyCharm.
- Add the desired arguments under the "Additional Arguments" field, for example:
  ```
  --hostname DESKTOP-C1OMGSH --port 6380 --foreground YES
  ```
- Apply the changes and run the tests.

## Project Structure

The project structure is as follows:

- `connection_handler`: Contains the connection handling logic.
- `steps`: Contains the test steps and utility functions.
- `test`: Contains the test cases.
- `binary`: Contains the binary files for the key-value store server.

## Testing

To run the tests, run it with pytest in pycharm or use command:
pytest
