import os

# Change directory to the project root
os.chdir('C:\\eazycart_automation')

# Run pytest with the specified test file
os.system('pytest testcases/test_login.py -v')