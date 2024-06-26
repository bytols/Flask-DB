from libCriptoSocket import CriptoSocket

cs = CriptoSocket('localhost', 4555)

for i in range(30):
    cs.enviar("MSG DE TESTE "+str(i))
    print(cs.receber())

cs.terminar()