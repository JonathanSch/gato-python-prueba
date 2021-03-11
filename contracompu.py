import time
import numpy as np

partida_terminada = False
eleccion_correcta = False

eleccion = raw_input('Como quieres jugar: solo o compu   ').lower()

if eleccion == 'solo' or eleccion == 'compu':
    eleccion_correcta = True

while eleccion_correcta == False:
    eleccion = raw_input('Como quieres jugar: solo o compu   ').lower()
    if eleccion == 'solo' or eleccion == 'compu':
        eleccion_correcta = True


linea1 = ['-','-','-']
linea2 = ['-','-','-']
linea3 = ['-','-','-']

numeros_escogidos = []
numeros_escogidos_x = []
numeros_escogidos_o = []


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
        printTablero()
        
    if(['O','O','O'] == fila1 or ['O','O','O']==fila2 or ['O','O','O']==fila3):
        partida_terminada = True
        printTablero()
        mensaje_ganar('O')
    if((fila1[0]== 'O' and fila2[0]== 'O' and fila3[0] == 'O') or (fila1[1]== 'O' and fila2[1]== 'O' and fila3[1] == 'O') or (fila1[2] == 'O' and fila2[2] == 'O' and fila3[2] == 'O')):
        partida_terminada = True
        printTablero()
        mensaje_ganar('O')
    if((fila1[0] == 'O' and fila2[1]=='O' and fila3[2]=='O') or (fila1[2] == 'O' and fila2[1]=='O' and fila3[0]=='O')):
        partida_terminada = True
        printTablero()
        mensaje_ganar('O')

    #Equis check

    if(['X','X','X'] == fila1 or ['X','X','X']==fila2 or ['X','X','X']==fila3):
        partida_terminada = True
        printTablero()
        mensaje_ganar('X')
    if((fila1[0]== 'X' and fila2[0]== 'X' and fila3[0] == 'X') or (fila1[1]== 'X' and fila2[1]== 'X' and fila3[1] == 'X') or (fila1[2]== 'X' and fila2[2]== 'X' and fila3[2] == 'X')):
        partida_terminada = True
        printTablero()
        mensaje_ganar('X')
    if((fila1[0] == 'X' and fila2[1]=='X' and fila3[2]=='X') or (fila1[2] == 'X' and fila2[1]=='X' and fila3[0]=='X')):
        partida_terminada = True
        printTablero()
        mensaje_ganar('X')

def anadir_numero(pedido,simbolo):
    if pedido== '1i':
        linea1[0] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='1m':
        linea1[1] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='1d':
        linea1[2] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='2i':
        linea2[0] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='2m':
        linea2[1] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='2d':
        linea2[2] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='3i':
        linea3[0] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='3m':
        linea3[1] = simbolo
        numeros_escogidos.append(pedido)
    elif pedido=='3d':
        linea3[2] = simbolo
        numeros_escogidos.append(pedido)

def eleccion_compu(row1,row2,row3,chosenX,chosen):
    if '1i' in numeros_escogidos_o and '1m' in numeros_escogidos_o and '1d' not in chosen:
        anadir_numero('1d','O')
        numeros_escogidos_o.append('1d')
    elif '1i' in numeros_escogidos_o and '1d' in numeros_escogidos_o and '1m' not in chosen:
        anadir_numero('1m','O')
        numeros_escogidos_o.append('1m')
    elif '1m' in numeros_escogidos_o and '1d' in numeros_escogidos_o and '1i' not in chosen:
        anadir_numero('1i','O')
        numeros_escogidos_o.append('1i')
    elif '2i' in numeros_escogidos_o and '2m' in numeros_escogidos_o and '2d' not in chosen:
        anadir_numero('2d','O')
        numeros_escogidos_o.append('2d')
    elif '2i' in numeros_escogidos_o and '2d' in numeros_escogidos_o and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in numeros_escogidos_o and '2d' in numeros_escogidos_o and '2i' not in chosen:
        anadir_numero('2i','O')
        numeros_escogidos_o.append('2i')
    elif '3i' in numeros_escogidos_o and '3m' in numeros_escogidos_o and '3d' not in chosen:
        anadir_numero('3d','O')
        numeros_escogidos_o.append('3d')
    elif '3i' in numeros_escogidos_o and '3d' in numeros_escogidos_o and '3m' not in chosen:
        anadir_numero('3m','O')
        numeros_escogidos_o.append('3m')
    elif '3m' in numeros_escogidos_o and '3d' in numeros_escogidos_o and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '1i' in numeros_escogidos_o and '2i' in numeros_escogidos_o and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '1i' in numeros_escogidos_o and '3i' in numeros_escogidos_o and '2i' not in chosen:
        anadir_numero('2i','O')
        numeros_escogidos_o.append('2i')
    elif '2i' in numeros_escogidos_o and '3i' in numeros_escogidos_o and '1i' not in chosen:
        anadir_numero('1i','O')
        numeros_escogidos_o.append('1i')
    elif '1m' in numeros_escogidos_o and '2m' in numeros_escogidos_o and '3m' not in chosen:
        anadir_numero('3m','O')
        numeros_escogidos_o.append('3m')
    elif '1m' in numeros_escogidos_o and '3m' in numeros_escogidos_o and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in numeros_escogidos_o and '3m' in numeros_escogidos_o and '1m' not in chosen:
        anadir_numero('1m','O')
        numeros_escogidos_o.append('1m')
    elif '1d' in numeros_escogidos_o and '2d' in numeros_escogidos_o and '3d' not in chosen:
        anadir_numero('3d','O')
        numeros_escogidos_o.append('3d')
    elif '1d' in numeros_escogidos_o and '3d' in numeros_escogidos_o and '2d' not in chosen:
        anadir_numero('2d','O')
        numeros_escogidos_o.append('2d')
    elif '2d' in numeros_escogidos_o and '3d' in numeros_escogidos_o and '1d' not in chosen:
        anadir_numero('1d','O')
        numeros_escogidos_o.append('1d')
    elif '1i' in numeros_escogidos_o and '2m' in numeros_escogidos_o and '3d' not in chosen:
        anadir_numero('3d','O')
        numeros_escogidos_o.append('3d')
    elif '1i' in numeros_escogidos_o and '3d' in numeros_escogidos_o and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in numeros_escogidos_o and '3d' in numeros_escogidos_o and '1i' not in chosen:
        anadir_numero('1i','O')
        numeros_escogidos_o.append('1i')
    elif '1d' in numeros_escogidos_o and '2m' in numeros_escogidos_o and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '1d' in numeros_escogidos_o and '3i' in numeros_escogidos_o and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in numeros_escogidos_o and '1d' in numeros_escogidos_o and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '1i' in chosenX and '1m' in chosenX and '1d' not in chosen:
        anadir_numero('1d','O')
        numeros_escogidos_o.append('1d')
    elif '1i' in chosenX and '1d' in chosenX and '1m' not in chosen:
        anadir_numero('1m','O')
        numeros_escogidos_o.append('1m')
    elif '1m' in chosenX and '1d' in chosenX and '1i' not in chosen:
        anadir_numero('1i','O')
        numeros_escogidos_o.append('1i')
    elif '2i' in chosenX and '2m' in chosenX and '2d' not in chosen:
        anadir_numero('2d','O')
        numeros_escogidos_o.append('2d')
    elif '2i' in chosenX and '2d' in chosenX and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in chosenX and '2d' in chosenX and '2i' not in chosen:
        anadir_numero('2i','O')
        numeros_escogidos_o.append('2i')
    elif '3i' in chosenX and '3m' in chosenX and '3d' not in chosen:
        anadir_numero('3d','O')
        numeros_escogidos_o.append('3d')
    elif '3i' in chosenX and '3d' in chosenX and '3m' not in chosen:
        anadir_numero('3m','O')
        numeros_escogidos_o.append('3m')
    elif '3m' in chosenX and '3d' in chosenX and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '1i' in chosenX and '2i' in chosenX and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '1i' in chosenX and '3i' in chosenX and '2i' not in chosen:
        anadir_numero('2i','O')
        numeros_escogidos_o.append('2i')
    elif '2i' in chosenX and '3i' in chosenX and '1i' not in chosen:
        anadir_numero('1i','O')
        numeros_escogidos_o.append('1i')
    elif '1m' in chosenX and '2m' in chosenX and '3m' not in chosen:
        anadir_numero('3m','O')
        numeros_escogidos_o.append('3m')
    elif '1m' in chosenX and '3m' in chosenX and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in chosenX and '3m' in chosenX and '1m' not in chosen:
        anadir_numero('1m','O')
        numeros_escogidos_o.append('1m')
    elif '1d' in chosenX and '2d' in chosenX and '3d' not in chosen:
        anadir_numero('3d','O')
        numeros_escogidos_o.append('3d')
    elif '1d' in chosenX and '3d' in chosenX and '2d' not in chosen:
        anadir_numero('2d','O')
        numeros_escogidos_o.append('2d')
    elif '2d' in chosenX and '3d' in chosenX and '1d' not in chosen:
        anadir_numero('1d','O')
        numeros_escogidos_o.append('1d')
    elif '1i' in chosenX and '2m' in chosenX and '3d' not in chosen:
        anadir_numero('3d','O')
        numeros_escogidos_o.append('3d')
    elif '1i' in chosenX and '3d' in chosenX and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in chosenX and '3d' in chosenX and '1i' not in chosen:
        anadir_numero('1i','O')
        numeros_escogidos_o.append('1i')
    elif '1d' in chosenX and '2m' in chosenX and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '1d' in chosenX and '3i' in chosenX and '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '2m' in chosenX and '1d' in chosenX and '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '2m' not in chosen:
        anadir_numero('2m','O')
        numeros_escogidos_o.append('2m')
    elif '1i' not in chosen:
        anadir_numero('1i','O')
        numeros_escogidos_o.append('1i')
    elif '1d' not in chosen:
        anadir_numero('1d','O')
        numeros_escogidos_o.append('1d')
    elif '3i' not in chosen:
        anadir_numero('3i','O')
        numeros_escogidos_o.append('3i')
    elif '3d' not in chosen:
        anadir_numero('3d','O')
        numeros_escogidos_o.append('3d')
    elif '1m' not in chosen:
        anadir_numero('1m','O')
        numeros_escogidos_o.append('1m')
    elif '3m' not in chosen:
        anadir_numero('3m','O')
        numeros_escogidos_o.append('3m')
    elif '2i' not in chosen:
        anadir_numero('2i','O')
        numeros_escogidos_o.append('2i')
    elif '2i' not in chosen:
        anadir_numero('2d','O')
        numeros_escogidos_o.append('2d')

turno = 0
respuestasAceptadas = ['1i','1m','1d','2i','2m','2d','3i','3m','3d']


while partida_terminada == False:
    if eleccion == 'solo':
        printTablero()
        pedido=raw_input('Turno de X  ' if turno%2==0 else 'Turno de los circulos  ')

        if pedido in numeros_escogidos:
            print('Espacio ya escogido')
            time.sleep(2)
            continue

        anadir_numero(pedido,'X' if turno % 2 == 0 else 'O')

        if pedido in respuestasAceptadas:
            turno+=1
        if pedido not in respuestasAceptadas: #Check if answer is accepted, not is like the ! in javascript
            print('Esa respuesta no esta aceptada')
            time.sleep(2)
        check_win_or_full(linea1,linea2,linea3)


    if eleccion == 'compu':
        if turno % 2 == 0:
            printTablero()
            pedido=raw_input('Turno de X  ' if turno%2==0 else 'Turno de los circulos  ')

            if pedido in numeros_escogidos:
                print('Espacio ya escogido')
                time.sleep(2)
                continue

            anadir_numero(pedido,'X')
            numeros_escogidos_x.append(pedido)
        else:
            eleccion_compu(linea1,linea2,linea3,numeros_escogidos_x,numeros_escogidos)


        if pedido in respuestasAceptadas:
            turno+=1
        if pedido not in respuestasAceptadas: #Check if answer is accepted, not is like the ! in javascript
            print('Esa respuesta no esta aceptada')
            time.sleep(2)
        check_win_or_full(linea1,linea2,linea3)