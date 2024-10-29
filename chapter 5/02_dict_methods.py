# Initial dictionary
marks = {
    "devil": 100,
    "happy": 90,
    "rohan": 80,
    0: "rahul"
}

# Print all items in the dictionary
print("Items:", marks.items())  # Print all items

# Print all keys in the dictionary
print("Keys:", marks.keys())  # Print the keys

# Print all values in the dictionary
print("Values:", marks.values())  # Print the values

# Update the marks and add a new entry
marks.update({"devil": 99, "jatin": 100})  # Update devil's score and add jatin
print("Updated marks:", marks)

# Using get() method to avoid KeyError
print("Get happy2:", marks.get("happy2"))  # Print None for non-existent key

# Uncommenting the line below would cause a KeyError
# print(marks["happy2"])  # This would raise a KeyError

# Using pop() method to remove a specific key
removed_value = marks.pop("happy", None)  # Remove 'happy' and return its value
print("Removed 'happy' with value:", removed_value)
print("Marks after pop:", marks)

# Using popitem() method to remove and return the last item
last_item = marks.popitem()  # Removes and returns the last inserted item
print("Removed last item:", last_item)
print("Marks after popitem:", marks)
