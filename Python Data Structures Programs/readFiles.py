# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    final = line.strip()
    print(final.upper())

