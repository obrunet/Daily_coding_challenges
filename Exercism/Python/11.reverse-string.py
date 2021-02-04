"""
Reverse a string
https://exercism.io/tracks/python/exercises/reverse-string/
For example: input: "cool" output: "looc"
"""

string = "This is a long string baby!"
print(string[::-1])

reverse = ""
for i in range(len(string)):
    reverse += string[-i-1]
print(reverse)

reverse_bis = "".join([string[-i-1] for i in range(len(string))])
print(reverse_bis)