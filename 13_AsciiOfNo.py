print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
	ascii = ord(char)
	print(char, "\t", ascii)
print("Length of the string is: ", textlength)
print("ASCII value of the string is: ", ascii)
