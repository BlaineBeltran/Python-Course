# Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

# This program with find the starting position of the desired number
# and convert the number to type float, then print

text = "X-DSPAM-Confidence:    0.8475"
new = text.find('0.8475')
print(new)
num = float(text[23:])
print(num)
