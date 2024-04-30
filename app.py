import os

def show_app_name():
    print("""
      Eat good restaurant
      """)

def show_options():
    print('1. Create new restaurant')
    print('2. List restaurants')
    print('3. Activate restaurant')
    print('4. Exit\n')

def shut_app_down():
    os.system('cls')
    print('Shutting app down')

def pick_options():
    
    option_chosen = int(input('Pick an option: '))

    if option_chosen == 1:
        print('Create new restaurant')
    elif option_chosen == 2:
        print('List restaurants')
    elif option_chosen == 3:
        print('Activate')
    else:
        shut_app_down()
    

def main():
    show_app_name() 
    show_options()
    pick_options()
    
    
if __name__ == '__main__':
    main()