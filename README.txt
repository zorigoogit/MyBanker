MyBanker
=================

Description:
A simple console application that performs basic banking operations including deposit and withdrawal transactions, as well as checking account balance.

Note: If you have already installed Python 3 or later and configured the system environment variables, you can skip steps I and II.


I. Install Python:
   1. Install Python 3.x (https://www.python.org/downloads/).
   Note: This program does not use any additional python libraries, so there is no need to install any additional dependencies

II. Environment Variables setup:
   1. Right-click 'This PC' > 'Properties' > 'Advanced system settings' > 'Environment Variables'.
   2. Edit 'Path' in 'System variables'.
   3. Add paths to Python and Scripts folders, installed on your machine(e.g., C:\Python311 and C:\Python311\Scripts). 
   4. Click 'OK' to save.

   MacOS/Linux:
   1. Open Terminal.
   2. Edit ~/.bashrc or ~/.zshrc with nano or another editor.
   3. Add: export PATH="/path/to/python:/path/to/scripts:$PATH".
   4. Save, then run source ~/.bashrc or source ~/.zshrc.
   This ensures the system recognizes Python and its scripts, letting you run Python and pip commands from anywhere.


III. Running the Build Script:
   1. Clone this repository to your local machine.
   2. Open a terminal or command prompt.
   3. Navigate to the project directory.
   4. Run the build script:
      - On Linux/macOS: `./build_script.sh`
      - On Windows: `build_script.bat`
   Note: The build script automatically performs unit test, compile source code and build deployable packages. 
   After the build script run successfully, following files and folders will be created automatically:
   - "unit_test_output.txt" - test result will be written in this file.
   - Distribution folder(named "dist") - deployable backages(wheel file, related backages and installation scripts) will be created in this folder.

IV. Installation
   1. run installation scripts (install.bat for Windows or install.sh for Linux/macOS)
   2. Alternatively, pip install MyBanker-0.1.0-py3-none-any.whl command also install the packages.

V. Using the Application:
   After installation, you can run the application by typing 'MyBanker' in the terminal or command prompt.









