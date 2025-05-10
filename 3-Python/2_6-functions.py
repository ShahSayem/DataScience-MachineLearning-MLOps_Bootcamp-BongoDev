### Built-in functions
name = "Shah Sayem AHMAD"
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())


my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
my_list = my_list[::-1]
print(my_list)


### Naming conventions
my_full_name = "Shah Sayem Ahmad" # Snake case
myFullName2 = "Shah Sayem Ahmad" # Camel case
print(my_full_name)


### User defined functions
def sum(a, b):
    return a+b

print(sum(2, 3))


def print_name(f_name, l_name):
    print(f_name, l_name)


print_name("Shah Sayem", "Ahmad")
