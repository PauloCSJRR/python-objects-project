import os

restaurants = [{'name':'Praça', 'category':'Sushi','active':False},
               {'name':'Pizza Suprema', 'category':'Pizza','active':True}]

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
    category = input(f'Type the category of the restaruant {restaurant_name}: ')
    resturant_data = {'name': restaurant_name,
                      'category':category,
                      'active':False}
    
    restaurants.append(resturant_data)
    print(f'The restaurant {restaurant_name} has been created successfully!\n')
    back_to_main_menu()

def list_restaurants():
    show_subtitles('Listing all restaurants')
    
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        category = restaurant['category']
        status = restaurant['active']
        print(f'{restaurant_name} | {category} | {status}')  
        
    back_to_main_menu()
    
def status_update():
    show_subtitles('Update restaurant status')
    name_restaurant = input('Type the name of the restaurant you wish to update status: ')
    found_restaurant = False
    
    for restaurant in restaurants:
        if name_restaurant == restaurant['name']:
            found_restaurant = True
            restaurant['active'] = not restaurant['active']
            msg = f'Restaurant {name_restaurant} sucessfully activated' if restaurant['active'] else f'Restaurant {name_restaurant} deactivated sucessfully'
            print(msg)
    if not found_restaurant:
        print('Restaurant not found')
    
    back_to_main_menu()
    

def pick_options():
    
    try:
    
        option_chosen = int(input('Pick an option: '))

        if option_chosen == 1:
            create_new_restaurant()
        elif option_chosen == 2:
            list_restaurants()
        elif option_chosen == 3:
            status_update()
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