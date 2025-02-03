class MyClass:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Enter a string: ")

    def printString(self):
        print(self.my_string.upper())

obj = MyClass()
obj.getString()
obj.printString()
