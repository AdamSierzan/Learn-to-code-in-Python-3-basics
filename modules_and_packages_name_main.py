def func():
    print("Func() in One.Py")
print("Top level in One.py")

if __name__ == '__main__':
    print("One.py is being run directly")
else: 
    print('One.py has been imoprted')