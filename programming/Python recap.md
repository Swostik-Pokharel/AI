#python
#programming 

## OS Library:
Main use of os is to make file-handling easy . As the name says It Allows you to interact with the OS directly , hence you can do much more than file handling like running commands for the code . 
Quick manual:

```python
import os

os.getcwd()                           # Get current working directory
os.chdir('/path/to/folder')           # Change to a different directory
os.listdir('.')                       # List all files/folders in a directory
os.path.exists('file.txt')            # Check if file or folder exists
os.path.isfile('file.txt')            # Check if it's a file
os.path.isdir('folder')               # Check if it's a directory
os.mkdir('new_folder')                # Create a new folder
os.remove('file.txt')                 # Delete a file
os.rename('old.txt', 'new.txt')       # Rename a file
os.path.join('folder', 'file.txt')    # Join paths safely (handles slashes)
```
## Re library:
Re or Regex  stands for regular expressions and it has everything to do with string patterns. If we know that a certain dataset will be in a certain format we can use regex to define a pattern hence making it easier to identify the different parts of the dataset.
## Type-hints :
A type-hint is basically like a comment which tells what the expected datatype for a function is , since we don't have to declare variables in python unless we specify the datatype the user might enter the args in a different data-type. For eg:
``
```python
def search(data):
```
Here we don't know what we are supposed to put in , it might be a list , a tuple , a dictionary or even a long string .Also we don't know what it returns. So if we instead do:
```python
from typing import Dict,List

def search(data: List )->"Number"
	return result
#or even better
def search (data:List[int])->"Smallest number"
```
so now we know that this function takes in a list of numbers and then returns the smallest number.

