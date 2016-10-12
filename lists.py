#! python3

print('Lists')

x = [5,3,6,3,7,9,5,4,3]
names = ['Ania', 'Ala', 'Dorotka', 'Kuba']
print(x)

x.append(100) # adds element to the end of list
print(x)

x.insert(1,99) # adds item 99 in index 1
print(x)

x.remove(99) # remove element who have value 99
print(x)

x.remove(x[0]) # remove element with index 0
print(x)

print(x[3]) # get value from index 3
print(x[3:5]) # get slice
print(x[-1]) # get last element
print(names.index('Ala')) # get index of element
print(x.count(3)) # how many times item occurs

# Numbers sorted
x.sort()
print(x)

# Alphabetically sorted
names.sort();
print(names)


