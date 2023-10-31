import sys
import json
from ping3 import ping

repeat = True
array_input = []
servers = []
servers_running = []
ant = 0
server =""

def main():
    global repeat
    global ant
    global server
    if __name__=='__main__':
        if len(sys.argv)>2:
            ant=int(sys.argv[1])
            server = sys.argv[2]
            servers.append(server)
            array_input.append(ant)
            while repeat:
                ant = int(input("1. toevoegen|2. verwijderen|3. lijst tonen|stop met input 000"))
                if ant == 000:
                     repeat = False
                else:
                    serversAanpassen(ant)
    data = {
    "servers": servers,
    "numbers": array_input
    }
    json_string = json.dumps(data)
    with open("list.json", "w") as outfile:
        outfile.write(json_string)



def serversAanpassen(keuze):
            global array_input
            global servers
            match keuze:
                case 1:
                    server = input("geef ne server")
                    print("server toevoegen")
                    array_input.append(keuze)
                    servers.append(server)
                case 2:
                    print("server verwijderen")
                    del array_input[-1]
                    del servers[-1]
                case 3:
                    print("lijst tonen")
                    print(servers, array_input)
                case _:
                    print("niet geldig")

def check():
    global servers_running
    with open('list.json', 'r') as json_file:
        data = json.load(json_file)
        servers = data['servers']
    for i in range(len(servers)):
        resp = ping(servers[i])
        if resp == False:
            servers_running.append("false")
        else:
            servers_running.append("true")
        serverRun = {
            "servers": servers,
            "running": servers_running
            }
        json_string = json.dumps(serverRun)
        with open("final.json", "w") as outfile:
            outfile.write(json_string)
        with open('index.html', 'w') as html_file:
            html_file.write(f"""<!DOCTYPE html>
            <html>
            <head>
            <title>JSON Data Page</title>
            </head>
            <body>
            <h1>Mijn servers</h1>
            <pre">{json_string}</pre>
            </body>
            </html>""")

        
            
def modus():
    positie = input("Wilt u starten in management of in check")
    if positie == "management":
        main()
    elif positie == "check":
        check()
    else: 
         print("u moet een correcte positie geven")

modus()
