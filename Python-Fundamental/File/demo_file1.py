"""
Mode	Description
r	    Open a file for reading. (default)
w	    Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	    Open a file for exclusive creation. If the file already exists, the operation fails.
a	    Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	    Open in text mode. (default)
b	    Open in binary mode.
+	    Open a file for updating (reading and writing)

"""

# Reading Files in Python 
text = open('myfile.txt','r') 
print(text.read())
text.close()

# Exception Handling in Files

try:
    file1 = open('myfile.txt','r')
    read_content = file1.read()
    print(read_content)
finally:
    # close the file
    file1.close()

# Use of with...open Syntax
# In Python, we can use the with...open syntax to automatically close the file. For example,

with open('myfile.txt','r') as files:
    read_content = files.read()
    print(read_content)


# Writing to Files in Python
with open('test2.txt', 'w') as file2:
    # write contents to the test2.txt file
    file2.write('One: Text File write by code.')
    file2.write('Two : Line of text write by prgram')
