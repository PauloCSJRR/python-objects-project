import os

print("""
      Eat good restaurant
      """)

print('1. Create new restaurant')
print('2. List restaurants')
print('3. Activate restaurant')
print('4. Exit\n')

option_chosen = int(input('Pick an option: '))

def shut_app_down():
    os.system('cls')
    print('Shutting app down')

if option_chosen == 1:
    print('Create new restaurant')
elif option_chosen == 2:
    print('List restaurants')
elif option_chosen == 3:
    print('Activate')
else:
    shut_app_down()