# Detect double space in a string
name = "Harry is a good boy  and" #name string never change because immutable

print(name.find("  ")) # new string formed and print

print(name.replace("  "," "))
# string are immutable which means that you cannot change \n
# -by running function on them