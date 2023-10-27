import sys
import json 

array_input = []
if __name__=='__main__':
    if len(sys.argv)>1:
        ant = int(sys.argv[1])
        array_input.append(sys.argv[1])
        if ant == 1:
            print("U wilt een server toevoegen")
        elif ant == 2:
            print("U wilt een server verwijderen")
        elif ant == 3:
            print("U heeft gekozen voor de lijst te tonen")
        else:
            print("Geef een geldig ant")
        while ant not in [1,2,3]:
            ant = int(input("toevoegen = 1, verwijderen = 2, lijst tonen = 3"))
            array_input.append(sys.argv[1])
            if ant == 1:
                print("U wilt een server toevoegen")
            elif ant == 2:
                print("U wilt een server verwijderen")
            elif ant == 3:
                print("U heeft gekozen voor de lijst te tonen")
            else:
                print("Geef een geldig ant")


json_object = json.dumps(array_input)
with open("list.json", "w") as outfile:
    outfile.write(json_object)