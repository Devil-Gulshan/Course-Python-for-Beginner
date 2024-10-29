name = "sachin"
 
print(len(name)) # find the string lengenth 

print (name.endswith("in")) # end of string "in"?

print (name.startswith("sac")) # start of string "sac"?

print (name.capitalize()) # small to conver string fist cap letter 

# Example string
text = "  Hello, World!  "

# 1. Basic String Operations
print("Original text:", text)
print("Length of text:", len(text))  # Length

# 2. String Manipulation
print("Lowercase:", text.lower())          # Convert to lowercase
print("Uppercase:", text.upper())          # Convert to uppercase
print("Title case:", text.title())         # Title case
print("Capitalized:", text.capitalize())   # Capitalize first character
print("Stripped:", text.strip())           # Remove whitespace
print("Replaced:", text.replace("World", "Python"))  # Replace substring

# 3. Searching and Finding
print("Index of 'World':", text.find("World"))  # Find index
print("Count of 'o':", text.count("o"))          # Count occurrences
print("Does it contain 'Hello'? :", "Hello" in text)  # Check existence

# 4. Splitting and Joining
words = text.split(", ")  # Split into a list
print("Split words:", words)  # List of words
joined = " - ".join(words)  # Join list into a string
print("Joined words:", joined)  # Join with separator

# 5. Formatting
name = "Alice"
greeting = f"Hello, {name}!"  # Using f-string
print("Greeting:", greeting)  # Formatted string

# 6. Checking Content
print("Starts with '  Hello':", text.startswith("  Hello"))  # Check start
print("Ends with 'World!  ':", text.endswith("World!  "))  # Check end
print("Is digit:", text.isdigit())  # Check if all characters are digits

