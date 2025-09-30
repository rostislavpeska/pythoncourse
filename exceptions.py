try:
    y = 10/0
    print(y)
except ZeroDivisionError as exc:
    print("Can't divide by zero")
    print(exc)
    raise
except ValueError as ver:
    print("Wrong value type")
except Exception as e:
    print("some other error")
else:
    print("error didn't happen")
finally:
    print("runs every time")

print("Sbohem")