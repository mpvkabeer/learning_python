#Example of 
# functions
# global variables
# accessing files
# if for while
# array

from mydata import first_names, last_names

invited_users = []
user_array = []

def say_hello_world():
    print("Hello World")

def invite_user(name):
    global invited_users
    print(f'Hello {name}... Welcome Aboard.')
    invited_users.append(name)


def create_user_array():
    global user_array
    total_first_names = len(first_names)
    total_last_names = len(last_names)
    if total_first_names == total_last_names:
        i=0
        while (i<total_first_names):
            user_array.append(first_names[i]+' '+last_names[i])
            i+=1
    else:
        print('Size of first names array and last_names array are not same.')

def invite_all_users():
    global user_array
    for each_name in user_array:
        invite_user(each_name)
        if (len(invited_users) % 5) == 0:
            print(f'{len(invited_users)} users are invited so far')

def print_total():
    global invited_users
    print(f'Total users invited: {str(len(invited_users))}')


def process1():
    say_hello_world()
    create_user_array()
    invite_all_users()
    print_total()
    
def process2():
    print_total()
    say_hello_world()
    invite_all_users()
    create_user_array()
    
def process3():
    say_hello_world()
    print_total()
    create_user_array()
    invite_all_users()        

process1()
process2()
process3()