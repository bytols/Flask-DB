import socket as s, datetime as d, threading as t, time

def TimeServer():
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.bind(("localhost",5432))
    server.listen(10)
    cont = 0
    while cont < 30:
        cont += 1
        sockb, addr = server.accept()
        data_hora = d.datetime.now()
        data_hora_str = data_hora.strftime('%d/%m/%Y, %H:%M:%S')
        sockb.send(data_hora_str.encode(encoding="utf-8"))
        sockb.close()
    server.close()

t.Thread(target=TimeServer).start()
time.sleep(1)
for i in range(30):
    cliente = s.socket(s.AF_INET, s.SOCK_STREAM)
    cliente.connect(("localhost", 5432))
    print(str(cliente.recv(1024)))
    cliente.close()

    