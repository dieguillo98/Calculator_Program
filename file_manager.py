import os
# We defined 3 functions: create, update and read files
def create():
    with open(f'{file_name}', 'x') as new_file:
        new_file.close()
    print("File successfully created")

def update():

        text = input("Write the text: ")
        with open('data.txt','a') as update_file:
            update_file.write(f'{text}\n')
            update_file.close()
def read():
     with open('data.txt','r') as read_file:
          read = read_file.read()
          read_file.close()
          print(read)
            
while True:
    # This is goint be true until the user says stop running.
    running = True

    #user and fil_name are associated, if customer doesn't type "data.txt" cannot have access
    user = input("Name of the file: ")

    file_name = 'data.txt'
    # Here we use match to validate 4 posible options: create, update, read, delete or exit file.
    if user == file_name:
        try:

            print('''
                1. Create file
                2. Update file
                3. Read file
                4. Delete file
                5. Exit
                    ''')
            option = int(input("Select an option [1-5]: "))
            match option:
                case 1:
                    if os.path.exists('data.txt'):
                        print('File already exists')
                    else:
                         create()

                case 2:
                    if os.path.exists("data.txt"):
                             update()
                             print("File updated")
                    else:
                        create()
                        update()
                        print('File created and updated')

                case 3:
                      if os.path.exists('data.txt'):
                           read()
                      else:
                           print(f'File does not exist, please create one.')

                case 4:
                      if os.path.exists("data.txt"):
                           os.remove('data.txt')
                           print('File deleted successfully')
                      else:
                           print("File doesn't exist anymore")

                case 5:
                      running = False

                case default:
                    print("Invalid option, enter one number from 1 to 4")
        except:
            print('Something gone wrong!')
        
        # This statemente closes the program when user types 'q'
    elif user == 'q':
        print('Good bye!')
        break
        
    
    else:
        print('The file does not make match')
