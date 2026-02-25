"""
In this script, let's learn the basics of I/O operations in Python.

To output some content, use the `print` function.
To accept some value from the keyboard (STDIN), use the `input` function.
"""

print("Hello there! It's a beutiful day.")
username = input("What's your name? ")
usercity = input("Where are you from? ")
# print("Hi " + username + ". Hope you are having a great time.")
# print("Hi %s. How's weather in %s?" % (username, usercity))
# print("Hello {}, how's weather in {}".format(username, usercity))
print(f"Hello {username}, how's weather in {usercity}?")
