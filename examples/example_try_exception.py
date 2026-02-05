# Example for 
# try exception

def first_step():
    try:
        total_family_members = int(input('Total Family members: '))
        total_assets_in_inr = int(input('Total Assets (in INR): '))
        share = total_assets_in_inr/total_family_members
        print(f'Share per person (in INR): {share}')
    except ZeroDivisionError: 
        print('Total Family members cannot be zero')
    except ValueError:
        print('Please enter a valid input')
       
def first_step_without_error_handling():
    total_family_members = int(input('Total Family members: '))
    total_assets_in_inr = int(input('Total Assets (in INR): '))
    share = total_assets_in_inr/total_family_members
    print(f'Share per person (in INR): {share}')    
        
def second_step():
    print("Second step is running now")
    
first_step()
#first_step_without_error_handling()
second_step()