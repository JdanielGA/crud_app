from utils.screens import *
from utils.tools import *
from utils.seconds_screens import *
from utils.read_registers import *



def run ():

    clean_screen()
    welcome_screen()
    wait(2)

    while True:

        clean_screen()
        choice_main_menu = main_screen()

        if choice_main_menu == "1":
            pass

        elif choice_main_menu == "2":

            while True:
                clean_screen()
                choice = registers_screen()

                if choice == "1":
                    clean_screen()
                    search_register(read_csv())

                elif choice == "2":
                    registers = read_csv()
                    
                    for data in registers:
                        show_one_register(data)
                    
                    input("Press Enter key for return: ")

                elif choice == "3":
                    break

                    

        elif choice_main_menu == "3":
            clean_screen()
            choice = update_screen()

        elif choice_main_menu == "4":
            clean_screen()
            choice = delete_screen()

        elif choice_main_menu.lower() == "exit":
            clean_screen()
            print("Session ended, good bye")
            wait(2)
            clean_screen()
            break

        else:
            print("\n"+"Invalid input")
            wait(1)



if __name__ == "__main__":
    run()