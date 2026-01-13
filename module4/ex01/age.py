#!/usr/bin/env python

try:
    age = int(input("pls, tell me your age: "))
except ValueError:
    print("not a valid age")
except EOFError:
    print("EOF error")
except KeyboardInterrupt:
    print("\n pressed Ctrl - C - see you soon")
else:
    print("you are currently %i years old" % age)
    print("in 10 years, you'll be %i years old." % (age + 10))
    print("in 20 years, you'll be %i years old." % (age + 20))
    print("in 30 years, you'll be %i years old." % (age + 30))

    