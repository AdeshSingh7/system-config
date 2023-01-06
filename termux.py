#!/usr/bin/python3
import config, os

if __name__=='__main__':
    try:
        os.system('clear')
        print(f"\33[1;94m+-----------------------------------------------+\33[0m")
        print(f"\33[1;94m| >>> Welcome to the installation program ! <<< |\33[0m")
        print(f"\33[1;94m+-----------------------------------------------+\33[0m")
        print(f"\33[1;91m\u2712 Update the system and install a list of commonly used tools and libraries.\33[0m")
        config.config_termux(config.termux_tools, config.termux_modules)
    except KeyboardInterrupt:pass
    except Exception as Error:print(f'Error: {Error}')
    finally:exit()
