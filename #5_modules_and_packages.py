print("\n<Pip install and Pypi>\n")
#  Repository for open-source Python packages
#  To install any repository just put : pip install package_name
#  Search tips to search python packages : python package for ... (Anything you need)
print("\n<How create personal packages>\n")
#  Create a new file with : module_name.py
#  To put another module into the actual program we put : from module_name import function_name
#  Create a new folder : name_folder, next inside this folder we create a folder named : SubPackage
#  To make that python recognize the folder is a package we need to create a file named : __init__.py inside name_folder
#  And inside SubPackage we create another __init__.py file
#  Inside to name_folder we create a file named : some_main_script.py, and inside Subpackage we create
#  a file named : subscript.py
print("\n<__name__ and __main__>\n")


#  __name__ build variable
def function_1():
    print("FUNCT() IN ONE.PY")


print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')
