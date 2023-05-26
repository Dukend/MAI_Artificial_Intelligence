def getAns(question):
    ans = 'Нет'
    while True:
        ans = input(f"{question} (Да/Нет): ").lower()
        if ans in ['да', 'yes', 'д', 'y'] :
            ans = 'Да'
            break
        elif ans in ['нет', 'no', 'н', 'n']:
            ans = 'Нет'
            break
        else:
            print("Нужно ввести либо 'Да', либо 'Нет'")
    return ans