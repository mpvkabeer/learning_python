#Example print variables
print("Kabeer")
firstname = 'John'
lastname = 'Smith'
print('FullName: '+firstname+' '+lastname)
print(f'FullName: {firstname} {lastname}')
print(f'FullName (in Capital): {firstname.upper()} {lastname.upper()}')
print("This is Kabeer's laptop")
print('Name of this lab is "Big Data Lab"')
print('''
This is an example for printing(showing) paragraphs
and multiple lines of texts. 
Used in may scenario like emails, summary..etc
It also supports special characters like ' and "  
''')

print('*' * 10)

new_age = 2
print('Age: '+str(new_age))

#Example text to number conversion
birth_year = input("Enter your Birth Year: ")
print(type(birth_year))
if birth_year == '':
    birth_year = 2000
age = 2025 - int(birth_year)
print(f'Your Age: {age}')

bookname = "Core Python"
print('First letter: '+ bookname[0])
print('Last letter: '+ bookname[-1])
print('Last letter: '+ bookname[len(bookname)-1])
print('4th to 7th letters: '+ bookname[3:6])
print('All letters: '+ bookname)
print('All letters: '+ bookname[:])

sample_array = [1, 2, 3]
for element in sample_array:
    print(f'Each element in for loop: {str(element)}')

total = 0
for element in sample_array:
    total = total+element
    print('current total: '+ str(total))

print('Final total: '+ str(total))
    
    
for each_item in range(1, 10):
    print(f'Each item in for loop: {str(each_item)}')
    
for each_item in range(1, 10, 2):
    print(f'Each item in for loop (Odd number): {str(each_item)}')    
    
#TODO: Excercise: Nested Array    
sample_nested_array = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]

for each_sample_array in sample_nested_array:
    print('new row')
    for each_sample in each_sample_array:
        print(each_sample)


#Example While loop
i=1    
while i<=10:
    print("value of i: "+str(i))
    i += 1
print('while loop is completed')
    
number_array = [1,2,3,4]
print('Default Array: ')
print(number_array)
number_array.insert(0,0)
print('Array after adding a new item in the start')
print(number_array)
number_array.insert(4,76)
print('Array after adding a new item in the middle')
print(number_array)
number_array.sort()
print('Array after sorting the items')
print(number_array)
number_array.remove(76)
print('Array after removing 76')
print(number_array)
number_array.clear()
print('Array after clearing all the items')
print(number_array)


#Tuples
new_tuples = (1, "Hi", 3)
print(new_tuples)
print(new_tuples[1])
    
first, second, third = new_tuples
print('First item: '+str(first))
print('second item: '+str(second))
print('third item: '+str(third))


new_dictionary = {
    "name": "Kabeer",
    "age": 41,
    "education": {
        "degree": "B.E",
        "course": "CSE",
        "college": {
            "code": 7701,
            "name": "sfsfsdfgdf"
        }
    },
    "family_details": {
        "father":"",
        "mother": ""
    }
}

print(new_dictionary["name"])