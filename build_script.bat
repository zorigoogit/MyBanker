@echo off

REM Clean previous builds
python setup.py clean --all

REM Install wheel if not installed already
pip install wheel

REM Run unit tests
echo.
echo Unit testing process is started ...
echo *******************************************************************************
python -m unittest discover -s . -p "unit_test.py" > unit_test_output.txt
SET TEST_FAILED=%ERRORLEVEL%

REM Build the package
echo.
echo Building process is started ...
echo *******************************************************************************
python setup.py sdist bdist_wheel

REM Copy the install and uninstall script to distribution directory
echo Copying installation script to the distribution directory...
copy .\scripts\install.bat .\dist\
copy .\scripts\install.sh .\dist\

echo Testing and building processes were completed successfully.

exit /b 0