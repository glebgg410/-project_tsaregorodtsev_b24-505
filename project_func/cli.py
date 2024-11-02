import prompt
def welcome():
    while True:
        result = prompt.string('<command> exit - выйти из программы\n<command> help - справочная информация\nВведите команду: ')
        if (result.lower() != 'help') and (result.lower() != 'exit'):
            break
        print()
