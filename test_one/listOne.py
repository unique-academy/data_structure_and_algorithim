from xml.etree.ElementTree import tostring

fruits = ["apple", "banana", "cherry"]

print(fruits)

mixed = [1, "hello", 3.5, True]
numbers = list([10, 20, 30])

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

print('The number at index 0 is ' + str(numbers[0]))
print('The number at index 1 is ' + str(mixed[1]))