import sys
import json
from ping3 import ping
from jinja2 import Template
import time

repeat = True
array_input = []
servers = []
servers_running = []
ant = 0

def main(nr,test):
    global array_input
    global repeat
    global ant
    global servers
    ant=int(nr)
    server = test
    servers.append(server)
    array_input.append(ant)
    print(servers)
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
    run =True
    global servers
    global servers_running
    while run:
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
        with open('template.html', 'r') as template_file:
            template = Template(template_file.read())
        data = list(zip(servers, servers_running))
        rendered_html = template.render(data=data)
        with open('index.html', 'w') as html_file: 
            html_file.write(rendered_html)
        servers_running.clear()
        time.sleep(120)
        
                 
def modus():
    positie = input("Wilt u starten in management of in check")
    if positie == "management":
        if __name__=='__main__':
            if len(sys.argv)>2:
                main(sys.argv[1],sys.argv[2])
    elif positie == "check":
        check()
    else: 
         print("u moet een correcte positie geven")

modus()
