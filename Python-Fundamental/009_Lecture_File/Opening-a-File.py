'''Python File Handling is an important part of Python programming. It allows you to create, read, write, and delete files on your computer. In this tutorial, we will cover the basics of file handling in Python.
We will learn how to open a file, read its contents, write to it, and close it. We will also discuss different file modes and how to handle exceptions while working with files.
1- Opening a File
2- Reading a File
3- Writing to a File
4- Closing a File
5- Renaming a File
6- Deleting a File
7- File Methods
8- File Attributes
9- File Operations
10- File Modes
11- File Position
12- File Object
13- File Object Methods
14- File Object Attributes
15- File Object Operations
16- File Object Methods

Modes
1. 'r' - Read mode: Opens a file for reading. The file pointer is placed at the beginning of the file.
2. 'w' - Write mode: Opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
3. 'a' - Append mode: Opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
4. 'x' - Exclusive creation mode: Opens a file for exclusive creation. If the file already exists, it raises a FileExistsError.
5. 'r+' - Read and write mode: Opens a file for both reading and writing. The file pointer is placed at the beginning of the file.
6. 'w+' - Write and read mode: Opens a file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
7. 'a+' - Append and read mode: Opens a file for both appending and reading. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.

'''

file = open('myfile.txt', 'r')  # Open a file in read mode
print(file.read())  # Read the contents of the file
file.close()  # Close the file
# The 'r' mode is used to open a file for reading. If the file does not exist, it raises an error.

# file = open('myfile.txt', 'w')  # Open a file in write mode
# file.write('Hello, World!')  # Write to the file
# file.close()  # Close the file
# The 'w' mode is used to open a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# file = open('myfile.txt', 'a')  # Open a file in append mode
# file.write('Hello, World!')  # Append to the file
# file.close()  # Close the file
# The 'a' mode is used to open a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
# file = open('myfile.txt', 'x')  # Open a file in exclusive creation mode
# file.write('Hello, World!')  # Create a new file
# file.close()  # Close the file
# The 'x' mode is used to open a file for exclusive creation. If the file already exists, it raises a FileExistsError.
# file = open('myfile.txt', 'r+')  # Open a file in read and write mode
# file.write('Hello, World!')  # Write to the file
# file.close()  # Close the file
# The 'r+' mode is used to open a file for both reading and writing. The file pointer is placed at the beginning of the file.
# file = open('myfile.txt', 'w+')  # Open a file in write and read mode
# file.write('Hello, World!')  # Write to the file
# file.close()  # Close the file
# The 'w+' mode is used to open a file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# file = open('myfile.txt', 'a+')  # Open a file in append and read mode
# file.write('Hello, World!')  # Append to the file
# file.close()  # Close the file
# The 'a+' mode is used to open a file for both appending and reading. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.




print("========================== File Reading ==========================")
# Read a File
with open("myfile.txt",'r') as file:
    content = file.read()
    print(content) # Prints the whole file
    
    

print("========================== Read by Line ==========================")

with open("test2.txt",'r') as file:
    for line in file:
        print(line.strip()) # Prints each line of the file
        

print("========================== Read by spacific line ==========================")
with open("test2.txt","r") as file:
    line = file.readlines()
    print(line[0])


print("========================== Write to file ==========================")

with open("test2.txt","w") as file:
    file.write("This is text written by python\n")

with open("test2.txt","r") as file:
    content = file.read()
    print(content) # Prints the whole file
    
print("========================== Write Multi line to file ==========================")

line = ["This is line 1\n", "This is line 2\n", "This is line 3\n"]

with open("text_write_by_multi_line.txt","w")  as file:
    file.writelines(line)

with open("text_write_by_multi_line.txt","r") as file:
    content = file.read()
    print(content)
    
    
print("========================== Appending file ==========================")

with open("text_write_by_multi_line.txt","a") as file:
    file.write("This Appending line 4\n")
    
with open("text_write_by_multi_line.txt","r") as file:
    content = file.read()
    print(content)
    
    
print("========================== Working with Binary file ==========================")
# Binary file for non-text files like images, audio, etc.

with open("image.png","rb") as file:
    data = file.read()
    print(data[:10])

with open("image.png","wb") as file:
    file.write(data)
    
    
print("========================== Checking file if a file exist ==========================")

import os

if os.path.exists("test2.txt"):
    print("File exists")
else:
    print("File does not exist")
    
    
print("========================== Delete file ==========================")

if os.path.exists("test2.txt"):
    os.remove("file_delete.txt")
    print("File deleted")
    
    
print("========================== Read and Writing User input to file ==========================")

file_name = "user_file.txt"

with open(file_name,"w") as userFile:
    input_text = input("Enter text to write to file: ")
    userFile.write(input_text)
    
with open(file_name,"r") as userFile:
    content = userFile.read()
    print(content)