from os import system


def clear_screen():
    _ = system('clear')


def bash_command(user_in):
    _ = system(user_in)


def use_terminal():
    shell_command = input("root@kali:~# ")
    bash_command(shell_command)
    use_terminal()
