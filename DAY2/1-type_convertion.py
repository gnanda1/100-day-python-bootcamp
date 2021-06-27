name = input("What is your name?")
"""
length = len(name)
This will throw an error "TypeError: can only concatenate str (not "int") to str"
"""
length = str(len(name))
print("Your name has " + length + " characters.")
