print("Math GPT")
print("Intructions:")
print("1. Type your mode (even, arthimetic, geometry, percentage and exponents).")
o = input("Your mode")
if o == "arthimetic":
    print("Instructions:")
    print("1. Type your first number.")
    print("2. Type your operation (*, /, + and -).")
    print("3. Type your second number.")
    x = int(input(""))
    y = input("")
    z = int(input(""))
    if y == "+":
        print(x + z)
    else:
        if y == "-":
            print(x - z)
        else:
            if y == "*":
                print(x * z)
            else:
                if y == "/":
                    print(x / z)
else:
    if o == "even":
        f = int(input("Write your number"))
        if f % 2 == 0:
            print("even")
        else:
            print("odd")
    if o == "Geometry" or o == "geometry":
        print("Enter your angles to find if it is part of a triangle")
        x = input("Triangle or quadrilateral")
        if x == "Triangle" or x == "triangle":
            x = int(input(""))
            y = int(input(""))
            z = int(input(""))
            if x + y + z == 180:
                print("Yes. It is the angles of the triangle")
            else:
                print("No. It is not the angle of a triangle.")
        else:
            print("Enter your 4 angles to see that add up to 360")
            x = int(input(""))
            y = int(input(""))
            z = int(input(""))
            h = int(input(""))
            if x + y + z + h == 360:
                print("Yes it is angles of a quadrilateral")
                if x == y == z == h:
                    print("It is a rectangle or a square")
    else:
        if o == "percentage":
            x = int(input("Type your percentage"))
            y = int(input("Type your whole number"))
            z = "Your percentage is"
            print(z, x % y)
        else:
            if o == "exponent" or o == "exponents":
                f = input("Square or Cube")
                if f == "Square" or f == "square":
                    x = int(input("Type your number"))
                    print(x*x)
                else:
                    x = int(input("Type your number"))
                    print(x*x*x)