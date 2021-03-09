import time

partida_terminada = False

def printTablero():
    print(linea1)
    print(linea2)
    print(linea3)

def mensaje_ganar(ganador):
    print('Ganaron ' + ('los circulos' if ganador=='O' else 'las X'))
    time.sleep(3)

def check_win_or_full(fila1,fila2,fila3):

    global partida_terminada

    if turno == 9:
        partida_terminada = True
        
    if(['O','O','O'] == fila1 or ['O','O','O']==fila2 or ['O','O','O']==fila3):
        partida_terminada = True
        mensaje_ganar('O')
    if((fila1[0]== 'O' and fila2[0]== 'O' and fila3[0] == 'O') or (fila1[1]== 'O' and fila2[1]== 'O' and fila3[1] == 'O') or (fila1[2] == 'O' and fila2[2] == 'O' and fila3[2] == 'O')):
        partida_terminada = True
        mensaje_ganar('O')
    if((fila1[0] == 'O' and fila2[1]=='O' and fila3[2]=='O') or (fila1[2] == 'O' and fila2[1]=='O' and fila3[0]=='O')):
        partida_terminada = True
        mensaje_ganar('O')

    #Equis check

    if(['X','X','X'] == fila1 or ['X','X','X']==fila2 or ['X','X','X']==fila3):
        partida_terminada = True
        mensaje_ganar('X')
    if((fila1[0]== 'X' and fila2[0]== 'X' and fila3[0] == 'X') or (fila1[1]== 'X' and fila2[1]== 'X' and fila3[1] == 'X') or (fila1[2]== 'X' and fila2[2]== 'X' and fila3[2] == 'X')):
        partida_terminada = True
        mensaje_ganar('X')
    if((fila1[0] == 'X' and fila2[1]=='X' and fila3[2]=='X') or (fila1[2] == 'X' and fila2[1]=='X' and fila3[0]=='X')):
        partida_terminada = True
        mensaje_ganar('X')


linea1 = ['-','-','-']
linea2 = ['-','-','-']
linea3 = ['-','-','-']

numeros_escogidos = []

turno = 0
respuestasAceptadas = ['1i','1m','1d','2i','2m','2d','3i','3m','3d']

while partida_terminada == False:
    printTablero()
    pedido=raw_input('Turno de X  ' if turno%2==0 else 'Turno de los circulos  ')

    if pedido in numeros_escogidos:
        print('Espacio ya escogido')
        time.sleep(2)
        continue

    if pedido== '1i':
        linea1[0] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='1m':
        linea1[1] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='1d':
        linea1[2] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='2i':
        linea2[0] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='2m':
        linea2[1] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='2d':
        linea2[2] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='3i':
        linea3[0] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='3m':
        linea3[1] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    elif pedido=='3d':
        linea3[2] = 'X' if turno%2==0 else 'O'
        numeros_escogidos.append(pedido)
    if pedido in respuestasAceptadas:
        turno+=1
    if pedido not in respuestasAceptadas: #Check if answer is accepted, not is like the ! in javascript
        print('Esa respuesta no esta aceptada')
        time.sleep(2)
    check_win_or_full(linea1,linea2,linea3)