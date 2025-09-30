"""
try:
    f = open("file.txt", "r")
    result = f.read()
    print(result)
    f.close()
except FileNotFoundError as e:
    print("file was not found")


try:
    with open("file2.txt", "w") as f:
        f.writelines(["Ahoj", "\n..."])
except FileNotFoundError as e:
    print("file was not found")

"""

import pandas as pd

username_df = pd.read_csv("username.csv")
print(username_df)


