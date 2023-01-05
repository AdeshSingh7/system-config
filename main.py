#!/usr/bin/python3
from cv2 import line
import config, os

if __name__=='__main__':
    try:
        status = True
        while status:
            os.system('clear')
            print(f"\33[91;1m-------------------------------------------------------------------------------------\33[0m")
            print(f"\33[91;1mWelcome to the installation program! Please choose an option from the following menu:\33[0m")
            print(f"\33[91;1m-------------------------------------------------------------------------------------\33[0m")
            for item in config.main_menu_items:
                print(f'\33[92m{item}\33[0m')
            print(f"\33[91;1m-------------------------------------------------------------------------------------\33[0m")
            choice = input(f"\33[93;1mEnter your choice >>> \33[0m")
            if choice == 'a':
                config.Update()
            elif choice == 'b':
                config.Ngrok()
            elif choice == 'c':
                config.Wine()
            elif choice == 'd':
                config.Anydesk()
            elif choice == 'e':
                config.Whatsapp()
            elif choice == 'f':
                config.VisualStudio()
            elif choice == 'g':
                config.Slack()
            elif choice == 'h':
                config.Tag_Sync()
            elif choice == 'i':
                config.Clean()
            elif choice == 'q':
                print("\33[91;1mThank you for using this program. Goodbye!\33[0m")
                exit()
            else:print("\33[91;1mInvalid choice. Please try again.\33[0m")
    except KeyboardInterrupt:
        status = False
    except Exception as Error:print(f'Error: {Error}')
    finally:exit()
