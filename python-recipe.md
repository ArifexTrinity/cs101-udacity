### HtDP Recipe

1. Signature, Purpose, Stub
2. Define example and wrap in test case
3. Template and Inventory
4. Code the body
5. Test and Debug until correct



### Step 1: Signature, Purpose, Stub

##### Example

We are going to write a function called length, that takes a string as input and returns the length of the string.

##### Signature and Purpose

```
"""
String -> Number                       # signature
Return the length of the given string  # purpose
"""
```

##### Stub

```
"""
String -> Number                       # signature
Return the length of the given String  # purpose
"""

def length(s):                         # stub
	return 0
```


### Step 2: Define example and wrap in test case

Run the code and fail

```
"""
String -> Number                       # signature
Return the length of the given String  # purpose
"""

def length(s):                         # stub
	return 0

# examples and test cases
assert length("Python") == 6
assert length("HtDP-recipe") == 11
assert length("") == 0
```


### Step 3：Template and Inventory

```
"""
String -> Number                       # signature
Return the length of the given String  # purpose
"""

def length(s):                         # stub
	return 0

def length(s):                         # inventory, don't run this
	... s

# examples and test cases
assert length("Python") == 6
assert length("HtDP-recipe") == 11
assert length("") == 0
```

### Step 4: Code the body
```
"""
String -> Number                       # signature
Return the length of the given String  # purpose
"""

# def length(s):                         # stub
#	  return 0

# def length(s):                         # inventory, don't run this
# 	  ... s

def length(s):
	total = 0
	for c in s:
	    total += 1
	return total

# examples and test cases
assert length("Python") == 6
assert length("HtDP-recipe") == 11
assert length("") == 0
```



### Step 5: Test and Debug until correct

Run the code, if failed, debug the program until correct
Do some cleanup:

- put signature and purpose into the function
- delete stub and inventory

```
def length(s):
	"""
	String -> Number
	Return the length of the given String
	"""
	total = 0
	for c in s:
	    total += 1
	return total

# examples and test cases
assert length("Python") == 6
assert length("HtDP-recipe") == 11
assert length("") == 0
```