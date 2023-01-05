#!/usr/bin/python3
import config, os

if __name__=='__main__':
    try:
        status = True
        while status:
            os.system('clear')
            print(f"\33[1;94m+----------------------------------------------------------------------------------------------+\33[0m")
            print(f"\33[1;94m| >>> Welcome to the installation program! Please choose an option from the following menu <<< |\33[0m")
            print(f"\33[1;94m+----------------------------------------------------------------------------------------------+\33[0m")
            for item in config.main_menu_items:
                print(f'\33[92m{item}\33[0m')
            print(f"\33[1;94m+----------------------------------------------------------------------------------------------+\33[0m")
            choice = input(f"\33[1;93mEnter your choice >>> \33[0m")
            if choice == 'a':
                print(f"\33[1;91m\u2712 Update the system and install a list of commonly used tools and libraries.\33[0m")
                config.Update(config.tools, config.module)
            elif choice == 'b':
                print(f"\33[1;91m\u2712 Download and install Ngrok, a tool for creating secure tunnels to localhost.\33[0m")
                config.Ngrok(config.ngrok, config.ngrok_key)
            elif choice == 'c':
                print(f"\33[91m\u2712 Download and install Wine 7.0, a compatibility layer that allows users to run Windows applications on Linux.\33[0m")
                config.Wine()
            elif choice == 'd':
                print(f"\33[1;91m\u2712 Download and install Anydesk, a remote desktop application.\33[0m")
                config.Anydesk(config.anydesk)
            elif choice == 'e':
                print(f"\33[1;91m\u2712 Download and install Whatsapp for Linux using the Snap package manager.\33[0m")
                config.Whatsapp()
            elif choice == 'f':
                print(f"\33[1;91m\u2712 Download and install Visual Studio Code, a popular code editor.\33[0m")
                config.VisualStudio(config.visualstudio)
            elif choice == 'g':
                print(f"\33[1;91m\u2712 Download and install Slack, a communication and collaboration platform, using the Snap package manager.\33[0m")
                config.Slack()
            elif choice == 'h':
                print(f"\33[1;91m\u2712 Clone the Tag Sync repository from GitHub and install it.\33[0m")
                config.Tag_Sync()
            elif choice == 'i':
                print(f"\33[1;91m\u2712 Remove any unused or broken packages and clear the system's cache.\33[0m")
                config.Clean()
            elif choice == 'q':
                print("\33[1;91m\u2712 Thank you for using this program. Goodbye!\33[0m")
                exit()
            else:print("\33[1;91m\u2712 Invalid choice. Please try again.\33[0m")
    except KeyboardInterrupt:
        status = False
    except Exception as Error:print(f'Error: {Error}')
    finally:exit()
