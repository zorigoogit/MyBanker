#!/bin/bash

# Clean previous builds
python setup.py clean --all

#Install wheel if not installed already
pip install wheel

# Run unit tests
echo
echo "Unit testing process is started ..."
echo "*******************************************************************************"
python -m unittest discover -s . -p "unit_test.py" > unit_test_output.txt
TEST_FAILED=$?

# Build the package
echo
echo "Building process is started ..."
echo "*******************************************************************************"
python setup.py sdist bdist_wheel

# Copy the install and uninstall script to distribution directory
echo "Copying installation script to the distribution directory..."
cp ./scripts/install.bat ./dist/
cp ./scripts/install.sh ./dist/

if [ $TEST_FAILED -ne 0 ]; then
    # Using echo for colored output; terminal dependent
    echo -e "\033[0;31mWARNING: Some unit tests failed. Please check the output above and unit_test_output.txt for details.\033[0m"
else
    echo "Testing and building processes were completed successfully."
fi

echo "Press any key to exit..."
read -n 1 -s
exit 0
