# Python Comments

## Single-Line Comments

To write a comment, just add a `#` at the start of the line.

**Examples:**

```python
# This is a 'Single-Line Comment'
print("Hello Gaurav !! Above is a single line comment")

print("Hello Gaurav !!")  # Printing Hello World

print("Gaurav! Below is a single line comment")
# print("Python Program")

```

## Multi-Line Comments:

To write multi-line comments you can use `#` at each line or you can use the multiline string.

**Example 1:** The use of ‘#’.

```python
# Below is python code 
# assign te value of ab,c,d
a = 55
b = 44
c = 11
d = 9
```

**Example 2:** The use of multiline string.

```python
""" Below python program is an basic arthematic program 
that will do aurthematic operations in python ."""

a = 55
b = 44
c = 11
d = 9

print("The value of a+b is:  ", a + b)
print("The value of a-b is:  ", a - b)
print("The value of a/c is:  ", a / c)
print("The value of a", "%", "d is: ", a % d)

```

# Escape Sequence Characters

To insert characters that cannot be directly used in a string, we use an escape sequence character.

To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash  `\`  followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

```python
print("This doesnt "execute")
print("This will \" execute")
```

# More on Print statement
The syntax of a print statement looks something like this:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)

print(2, 4, 5, 7, sep='~') # sep=separator
print(2, 4, 5, 8, 11, end='Guarav') #end
print("Gaurav Kumar Singh") 
```

## Other Parameters of Print Statement 
1. object(s): Any object, and as many as you like. Will be converted to string before printed
2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' ' -(Optional)
3. end='end': Specify what to print at the end. Default is '\n' (line feed) - (Optional)
4. file: An object with a write method. Default is sys.stdout - (Optional)


# Variables

Python Variable is containers that store values.

```python
a = 5
b = "Gaurav"
c = True
d = None

print(a)
print(b)
print(c)
print(d)
```

# Data Type

Data type specifies the type of value a variable holds. In python, we can print the type of any operator using type function:

```python
a = 1
print(type(a))
b = "1"
print(type(b))
```

