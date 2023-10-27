import sys
if __name__=='__main__':
    if len(sys.argv > 1):
        ant = sys.argv
        if ant == 1:
            print("U wilt een server toevoegen")
        elif ant == 2:
            print("U wilt een server verwijderen")
        elif ant == 3:
            print("U heeft gekozen voor de lijst te tonen")
        else:
            print("Geef een geldig ant")

