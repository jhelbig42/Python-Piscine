#!/usr/bin/env python

try:
    first = int(input("give me the first number: "))
    second = int(input("give me the second number: "))
except ValueError:
    print("invalid input")
except EOFError:
    print("ctrl-D pressed. Goodbye")
except KeyboardInterrupt:
    print("ctrl-C pressed. Goodbye")
else:
    print("Thank you")
    print("%i + %i = %i" % (first, second, (first + second)))
    print("%i - %i = %i" % (first, second, (first - second)))
    if (second != 0):
        print("%i / %i = %f" % (first, second, (first / second)))
    else:
        print("Division by zero is not possible")
    print("%i * %i = %i" % (first, second, (first * second)))