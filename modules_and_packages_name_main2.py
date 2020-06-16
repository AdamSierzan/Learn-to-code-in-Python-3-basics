import modules_and_packages_name_main

print("Top level in two.py")

modules_and_packages_name_main.func()

if __name__ == '__main__':
    print("Two.py is being run directly ")
else:
    print("Two.py has been imported")