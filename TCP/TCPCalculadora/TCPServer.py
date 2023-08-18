from socket import *

serverPort = 12002
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

serverSocket.listen()

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

while 1:
       #Cria um socket para tratar a conexao do cliente
     

     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024)
     sentence = sentence.decode().split()
     resultado = "erro de digitacao :( tente de novo escrevendo em portugues as opercaoes soma subtrracao etc"
     if sentence[0] ==  "soma":
        resultado = int(sentence[1]) + int(sentence[2])
     elif sentence[0] == "subtracao":
        resultado = int(sentence[1]) - int(sentence[2])
     elif sentence[0] == "multiplicacao":
        resultado = int(sentence[1]) * int(sentence[2])
     elif sentence[0] == "divisao":
        resultado = int(sentence[1]) / int(sentence[2])    

     connectionSocket.send(str(resultado).encode('ascii'))
     connectionSocket.close()