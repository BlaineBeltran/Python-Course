# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt

fname = input('Enter file name: ')
fhand = open(fname)

print(fhand)
# for line in fhand:
#     print(line.upper())