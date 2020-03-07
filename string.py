# Single line String

a = 'Hello World '
print(a,"\n")

# Multiline String

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(b,"\n")

# Strings are like array

print("Second Character of a: ",a[1],"\n")
print("Last Character of a: ",a[-1],"\n")

# Slicing

print("Second Character to Fifth Character of a: ",a[1:5],"\n")

# Length of a string

print("Length of a: ", len(a))

# Combining two Strings

d = "Hello"
e = "World"
print("Combining d and e: ",d+e)

# String Methods

## The strip() method removes any whitespace from the beginning or the end:

print("Stripped String: ",a.strip(),"\n") # returns "Hello, World"

## The lower() method returns the string in lower case:

print("All lowercase: ",a.lower(),"\n")

## The upper() method returns the string in upper case:

print("All uppercase: ",a.upper(),"\n")

## The replace() method replaces a string with another string:

print("Replacing H with J: ",a.replace("H", "J"),"\n")




