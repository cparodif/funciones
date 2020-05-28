#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time, sys, os
from sys import path
path.append('./')

def crear_fichero_resultados():
    texto_cabecera = "cabecera"
    file = open("./resultados.txt", "w")
    file.write(texto_cabecera)
    file.close()
    return

def abrir_fichero_resultados():
    file = open("./resultados.txt", "w")
    return file

def cerrar_fichero_resultados(pfile):
    pfile.close()
    return

def escribir_nueva_linea_en_fichero_resultados(ptexto, pfile):
    pfile.write(ptexto+"\n")
    return

def abrir_fichero_datos_CanBus():
    file = open("./Old_truck_7.txt", "r")
    return file

def leer_en_fichero_datos_CanBus_una_linea(pfile):
    linea = pfile.readline()
    return linea

def cerrar_fichero_datos_CanBus(pfile):
    pfile.close()
    return

def abrir_fichero_datos_J1939DA():
    file = open("./J1939DA_201907_PGNs & SPNs.csv", "r")
    return file

def leer_en_fichero_datos_J1939DA_una_linea(pfile):
    linea = pfile.readline()
    return linea

def cerrar_fichero_datos_J1939DA(pfile):
    pfile.close()
    return

def almacenar_fichero_datos_J1939DA_a_una_matriz():
    ficheroJ1939DA=abrir_fichero_datos_J1939DA()
    primeraLinea = leer_en_fichero_datos_J1939DA_una_linea(ficheroJ1939DA)
    m=0
    y=[]
    for nuevaLineaJ1939DA  in ficheroJ1939DA:
        x1 = nuevaLineaJ1939DA.replace('\n','')
        x2 = x1.split(',')
        y.append(x2)
        m = m + 1
        if (m > 1000):
            break
    return y


def calcularCanId(p):
    x = "0"+p[:-1]
    x = x[-8:]
    return x

def hexadecimalEnBinario(p):
    valoresHexadecimalBinario={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',
        '6':'0110','7':'0111','8':'1000','9':'1001','a':'1010','b':'1011',
        'c':'1100','d':'1101','e':'1110','f':'1111'}
    x=[]
    p=p.lower()
    for i in p:
        if i in valoresHexadecimalBinario:
            x.append(valoresHexadecimalBinario[i])
    return ("").join(x)

def binarioAgrupado(x):
    #x='00001100111100000000001100000000'
    x = x[0:4] + ' '+ x[4:8] + '  '+ x[8:12] +' '+ x[12:16] +'  '+ x[16:20] +' '+ x[20:24] +'  '+ x[24:28] +' '+ x[28:32]
    return x

def Priority(x):
    x= str(x[3:6])
    return x

def R(x):
    x= str(x[6:7])
    return x

def DP(x):
    x= str(x[7:8])
    return x

def PF(x):
    x= str(x[8:16])
    return x

def PFd(x):
    x = str(int(x, 2))
    return x

def PS(x):
    x= str(x[16:24])
    return x

def ECU(x):
    x= str(x[24:])
    return x

def Tipo(p):
    x=int(PFd(PF(p)))
    # tipo en función del valor de PF
    if x >=0 and x<=239:
        return 1 #Tipo 1
    elif x >=240 and x<=255:
        return 2 # Tipo 2
    else:
        return 0 # Tipo desconocido

def PGN(x):
    aR = R(x)
    aDP = DP(x)
    aPF = PF(x)
    aPS = PS(x)
    if Tipo(x) == 1:
        return aR+aDP+aPF+'00000000'
    else:
        return aR+aDP+aPF+aPS

def PGNd(p):
    x = PGN(p)
    x = str(int(str(x), 2))
    return x


def calcularTrama(p):
    trama = p[2:25]
    return trama

def calcularTramab(p):
    x=hexadecimalEnBinario(calcularTrama(p))
    return x

def pasarArrayATexto(x):
    y = ""
    for l in x:
        y += " "+l
    return y
'''
def convertHextoDec(x):
    return str(int(x, 16))

def PNGhex(x):
    longitud = len(x)
    if longitud == 8:
        x=x[1:5]
        return x
    elif longitud == 9:
        x=x[2:6]
        return x
    else:
        return 0

def obtenerbinario(x):
    x = x[:-1]
    x = bin(int(x, scale))[2:].zfill(32)
    #binariocero = bin(int(cero, scale))[2:].zfill(num_of_bits)
    #binary_string = binascii.unhexlify(x)
    return x#binary_string







def esSenialDelVehiculo(x):
    if x=='18ecff00': # TPCM ec00x
        return "no"
    elif x == '18ebff00': # TPDP eb00x
        return "no"
    elif x == '18eaff28': # RQST ea00x
        return "no"
    else:
        return "si"



def calcularResultado1(pNuevaLinea):
    partesDeLaLinea = pNuevaLinea.split('  ')
    resultado = "->"
    pl0 = partesDeLaLinea[0]
    resultado += pl0 + " - "
    pl1 = partesDeLaLinea[1]
    resultado += pl1 + " - "
    pl2 = partesDeLaLinea[2]
    resultado += pl2 + " - "
    canId1 = partesDeLaLinea[3]
    resultado += " canId1= "+ canId1 + " - "
    pl4 = partesDeLaLinea[4]
    resultado += pl4 + " - "
    pl5 = partesDeLaLinea[5]
    resultado += pl5 + " - "
    trama1 = partesDeLaLinea[6]
    resultado += " trama1= " + trama1 + " - "
    resultado += "origen = " + pNuevaLinea


    canIdh=calcularCanId(canId1)
    trama=calcularTrama(trama1)
    tramab=calcularTramab(trama1)
    resultado = ""
    resultado = resultado + " canIdh="+ canIdh + ", "
    canIdb=hexadecimalEnBinario(canIdh)
    resultado = resultado + " canIdb="+ canIdb + ", "
    canIda=binarioAgrupado(canIdb)
    resultado = resultado + " canIda="+ canIda + ", "
    resultado += " prioridad =" + Priority(canIdb)
    resultado += " R =" + R(canIdb)
    resultado += " DP =" + DP(canIdb)
    resultado += " PF =" + PF(canIdb)
    resultado += " PFd =" + PFd(PF(canIdb))
    resultado += " PS =" + PS(canIdb)
    resultado += " ECU =" + ECU(canIdb)
    resultado += " Tipo =" + str(Tipo(canIdb))
    resultado += " PGN =" + str(PGN(canIdb))
    resultado += " PGNd =" + str(PGNd(canIdb))
    resultado += " Tipo =" + str(Tipo(canIdb))
    resultado += " EsSeñaldelVehiculo =" + esSenialDelVehiculo(canIdh)
    resultado += " trama=" + trama
    resultado += " tramab=" + tramab
    resultado += "origen = " + pNuevaLinea

    resultado = ""
    resultado = resultado + "canIdh="+ canIdh + ", "
    resultado += " PGNd =" + str(PGNd(canIdb))
    resultado += " Tipo =" + str(Tipo(canIdb))
    resultado += " EsSeñaldelVehiculo =" + esSenialDelVehiculo(canIdh)
    resultado += " trama=" + trama
    resultado += " tramab=" + tramab
    resultado += "   origen = " + pNuevaLinea
    return [canIdh, str(PGNd(canIdb)), tramab, resultado]

def calcularResultado2(pNuevaLinea):
    partesDeLaLinea = pNuevaLinea.split('  ')
    canId1 = partesDeLaLinea[3]
    trama1 = partesDeLaLinea[6]
    canIdh=calcularCanId(canId1)
    canIdb=hexadecimalEnBinario(canIdh)
    trama=calcularTrama(trama1)
    tramab=calcularTramab(trama1)
    resultado = ""
    resultado = resultado + "canIdh="+ canIdh + ", "
    resultado += " PGNd =" + str(PGNd(canIdb))
    resultado += " Tipo =" + str(Tipo(canIdb))
    resultado += " trama=" + trama
    resultado += " tramab=" + tramab
    resultado += "   origen = " + pNuevaLinea
    return [canIdh, str(PGNd(canIdb)), trama, resultado]
'''
