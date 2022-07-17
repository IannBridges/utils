"""
NAME
    ptree - list contents of a text file in a tree like format
SYNOPSIS
    tree [-f file]
FUNCTION
    given a text file with text indented by tabs, tree displays the file with the text organized into a tree like format. Useful for creating a visually appealing "theorem trees", etc. 
"""
import sys
text = sys.argv
output = ""
with open(str(text[1]), "r") as file:
    content = file.read()
    for char in content:
        if char == '\t':
            output += str(rb'\U00002014'.decode("unicode_escape"))
            output += " "
        elif char == '\n':
            output += "\n|"
        else:
            output += char
print(output)
