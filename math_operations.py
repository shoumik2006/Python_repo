class Math_Operations:
    

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def divide(self, x, y):
        return x / y

    def multiply(self, x, y):
        return x * y

operations = Math_Operations()
x = int(input("First Number: "))
y = int(input("Second Number: "))
print("add", operations.add(x,y))
print("subtract", operations.subtract(x,y))
print("division", operations.divide(x,y))
print("multiplication", operations.multiply(x,y))

