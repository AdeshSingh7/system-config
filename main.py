#!/usr/bin/python3
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
                print(f'Updating installation')
                config.Update(config.tools, config.module)
            elif choice == 'b':
                print(f'Installing Ngrok')
                config.Ngrok(config.ngrok, config.ngrok_key)
            elif choice == 'c':
                print(f'Installing Wine')
                config.Wine()
            elif choice == 'd':
                print(f'Installing Anydesk')
                config.Anydesk(config.anydesk)
            elif choice == 'e':
                print(f'Installing Whatsapp')
                config.Whatsapp()
            elif choice == 'f':
                print(f'Installing Visual Studio')
                config.VisualStudio(config.visualstudio)
            elif choice == 'g':
                print(f'Installing Slack')
                config.Slack()
            elif choice == 'h':
                print(f'Installing Tag Sync')
                config.Tag_Sync()
            elif choice == 'i':
                print(f'Cleaning')
                config.Clean()
            elif choice == 'q':
                print("\33[91;1mThank you for using this program. Goodbye!\33[0m")
                exit()
            else:print("\33[91;1mInvalid choice. Please try again.\33[0m")
    except KeyboardInterrupt:
        status = False
    except Exception as Error:print(f'Error: {Error}')
    finally:exit()
