### List
students = ["Sayem", "Sami", "Shahriar", "Shakib"]
students.append("Anku")
print(len(students))

students.insert(3, "Samiul")
print(students)
students.remove("Sami")
print(students)

students[1] = "Ferdous" #Lists are mutable
print(students)

print(students[0])
# Slicing
print(students[0:3]) # 0 to 2

### String
my_line = "This is a line!"
print(len(my_line))

#my_line[0] = 't' # This will raise an error because strings are immutable
print(my_line[0:6]) # 0 to 5


### Dictionary: key-value pair
sayem = {
    "name": "Sayem",
    "age": 22,
    "is_student": True,
    "courses": ["Python", "Java", "C++"]
}

sayem["age"] = 24 # Dictionary is mutable

print(sayem["name"])
print(sayem["age"])
print(sayem["courses"][1]) # Accessing list inside dictionary

sayem["occupation"] = "Software Engineer" # Adding new key-value pair
sayem.pop("is_student") # Removing key-value pair
print(sayem)


### Set: unordered collection of unique elements
# numbers = {1, 2, 3, 4, 5, 5, 5, [1, 2, 3], 3.1416, "Sayem"} 
numbers = {1, 2, 3, 4, 5, 5, 5} 
print(numbers) # {1, 2, 3, 4, 5}
numbers.add(6) # Adding element 

even = [2, 4, 6, 6, 6, 6, 8]
even_set = set(even) # Converting list to set
print(even_set) # {2, 4, 6, 8}


### Tuple: immutable collection of elements (immutable list)
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) # 1

# my_tuple[0] = 10 # This will raise an error because tuples are immutable

### Data types: str, int, float, bool, list, dict, set, tuple