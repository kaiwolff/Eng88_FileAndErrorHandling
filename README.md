# Files and Error Handling

## Errors and Exception handling

`try` `except` and `finally` blocks are the core of error handling.

`try` is the first attempt. This is what the code will attempt first

`except` will run if the try attempt throws an error. This can be set to 

`finally` works as an else statement would - should the except block not trigger


In Practice, one of these looks like this:

```python
try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    #creating aliases. The as portion defines the error message as a variable
    print("order.txt not found\n" + str(errmsg))
finally:
    print("Thank you for visiting, hope to see you again!")
    #This will run, regardless of whether the other blocks run.
```

The try portion will only work if there is a file with the given name in the directory, otherwise the except block will kick in. The ```finally``` will trigger at the end.

### Handling files - Reading files



- We have already opened a file and we have begun to handle some of the errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening



`open(file, mode)`



| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|