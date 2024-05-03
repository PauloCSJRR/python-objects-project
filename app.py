import os

restaurants = [{'nome':'Praça', 'ativo':False},
               {'nome':'Pizza Suprema', 'ativo':True}]

def show_subtitles(text):
    os.system('cls')
    print(text)

def back_to_main_menu():
    input('\nType any character to return to main menu ')
    main()

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
    show_subtitles('Shutting app down')

def invalid_option():
    print('Invalid option\n')
    back_to_main_menu()

def create_new_restaurant():
    show_subtitles('Create new restaurant')
    restaurant_name = input("What's the name of the restaurant? ")
    restaurants.append(restaurant_name)
    print(f'The restaurant {restaurant_name} has been created successfully!\n')
    back_to_main_menu()

def list_restaurants():
    show_subtitles('Listing all restaurants')
    
    for restaurant in restaurants:
        restaurant_name = restaurant['nome']
        status = restaurant['ativo']
        print(f'Restaurant: {restaurant_name}, status: {status}')  
        
    back_to_main_menu()
    

def pick_options():
    
    try:
    
        option_chosen = int(input('Pick an option: '))

        if option_chosen == 1:
            create_new_restaurant()
        elif option_chosen == 2:
            list_restaurants()
        elif option_chosen == 3:
            print('Activate')
        elif option_chosen == 4:
            shut_app_down()
        else:
            invalid_option()
            
    except:
        invalid_option()

def main():
    os.system('cls')
    show_app_name() 
    show_options()
    pick_options()
    
    
if __name__ == '__main__':
    main()