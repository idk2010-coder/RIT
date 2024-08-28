print("Math GPT")
print("Intructions:")
print("1. Type the first number.")
print("2. Type your operation (+, -, * and /)")
print("3. Type the second number")
print("4. Your answer is ready")
x = int(input(""))
y = input("")
z = int(input(""))
if y == "+":
    print(x + z)
else:
    if y == "-":
        print(x - z)
    if y == "*":
        print(x * z)
    if y == "/":
        print(x/z)