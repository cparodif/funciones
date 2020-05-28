#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time, sys, os
from sys import path
path.append('./')
from funciones import *

def calcularResultado(pNuevaLinea):
    x1 = pNuevaLinea.replace('\n','')
    partesDeLaLinea = x1.split('  ')
    canId1 = partesDeLaLinea[3]
    trama1 = partesDeLaLinea[6]
    canIdh=calcularCanId(canId1)
    canIdb=hexadecimalEnBinario(canIdh)
    trama=calcularTrama(trama1)
    tramab=calcularTramab(trama1)
    resultado = ""
    resultado +=  pNuevaLinea
    return [canIdh, str(PGNd(canIdb)), trama, resultado]


def numeroDeBits(pLongitud):
    pLongitud.strip()
    y=0
    if (pLongitud == "1 bit"):
         y = 1
    if (pLongitud == "2 bits"):
         y = 2
    if (pLongitud == "3 bits"):
         y = 3
    if (pLongitud == "4 bits"):
         y = 4
    if (pLongitud == "5 bits"):
        y = 5
    if (pLongitud == "6 bits"):
        y = 6
    if (pLongitud == "7 bits"):
        y = 7
    if (pLongitud == "8 bits"):
        y = 8
    if (pLongitud == "9 bits"):
        y = 9
    if (pLongitud == "10 bits"):
        y = 10
    if (pLongitud == "1 byte"):
        y = 8
    if (pLongitud == "2 bytes"):
        y = 16
    if (pLongitud == "3 bytes"):
        y = 24
    if (pLongitud == "4 bytes"):
        y = 32
    return y

def extraexBitsParaAnalizarValidez(pTramah, pPosicion, pLongitud):
# extraexBitsParaAnalizarValidez("00 00 00 0c 06 54 23 41", "1.3", "2 bits"):
    pTramah.strip()
    pTrama = pTramah.split(" ")
    y = numeroDeBits(pLongitud)
    datosParaAnalizar=""
    # posicion "1.3" o "2-3"
    #pTrama[0] = pTramah[0:2]
    #pTrama[1] = pTramah[3:5]
    #pTrama[2] = pTramah[6:8]
    #pTrama[3] = pTramah[9:11]
    #pTrama[4] = pTramah[12:14]
    #pTrama[5] = pTramah[15:17]
    #pTrama[6] = pTramah[18:20]
    #pTrama[7] = pTramah[21:23]

    numCaracteres = len(pPosicion)

    if (numCaracteres == 1):
        x = int(pPosicion[0])
        datosParaAnalizar = hexadecimalEnBinario(pTrama[x])

    if (numCaracteres == 3):
        if (pPosicion[1] == "."):
            x1= int(pPosicion[0])-1
            x2= int(pPosicion[2])-1
            datosParaAnalizar = hexadecimalEnBinario(pTrama[x1])
            datosParaAnalizar = datosParaAnalizar[x2:x2+y]

        if (pPosicion[1] == "-"):
            #inluir los dos bytes, de la trama pero en orden inverso
            x1 = int(pPosicion[0])-1
            x2 = int(pPosicion[2])-1
            datosParaAnalizar = hexadecimalEnBinario(pTrama[x2])+hexadecimalEnBinario(pTrama[x1])

    return datosParaAnalizar

def datosEstanDisponibles(x):
    # x = DatosParaAnalizar
    for i in range(len(x)):
        if (x[i] == "0"):
            return "Datos disponibles"
    return "Datos no disponibles"

def contienenSenalesValidasDelVehiculo(x):
    #x es el PGNdLineaCanBus
    if (x == "60416"):
        return False
    elif (x == "60160"):
        return False
    elif (x == "59904"):
        return False
    else:
        return True


def main():
    ficheroCanBus = abrir_fichero_datos_CanBus()
    ficheroJ1939DA = abrir_fichero_datos_J1939DA()
    datosJ1939DA = almacenar_fichero_datos_J1939DA_a_una_matriz()
    crear_fichero_resultados()
    ficheroResultados = abrir_fichero_resultados()

    n=0
    primeraLinea = leer_en_fichero_datos_CanBus_una_linea(ficheroCanBus)
    segundaLinea = leer_en_fichero_datos_CanBus_una_linea(ficheroCanBus)
    print(primeraLinea)
    print(segundaLinea)
    escribir_nueva_linea_en_fichero_resultados(primeraLinea,ficheroResultados)
    escribir_nueva_linea_en_fichero_resultados(segundaLinea,ficheroResultados)
    for nuevaLineaCanBus  in ficheroCanBus:
        n=n+1
        m=0
        encontrado = 0
        lineaResultado = calcularResultado(nuevaLineaCanBus)
        canIdH=lineaResultado[0]
        PGNdLineaCanBus = lineaResultado[1]
        trama = lineaResultado[2]
        tramab=calcularTramab(trama)
        original = lineaResultado[3].replace('\n','')
        p1="CanId="+canIdH+" PNGd="+PGNdLineaCanBus+" Trama="+trama+" Trama="+binarioAgrupado(tramab)
        print(original)
        escribir_nueva_linea_en_fichero_resultados("\n"+"Del CanBus --------------> "+original+" <-------------- ",ficheroResultados)
        escribir_nueva_linea_en_fichero_resultados(p1,ficheroResultados)
        if (contienenSenalesValidasDelVehiculo(PGNdLineaCanBus)):
            for nuevaLineaJ1939DA  in datosJ1939DA:
                m=m+1
                PGNdLineaJ1939DA = nuevaLineaJ1939DA[0]
                spPositionPgLineaJ1939DA = nuevaLineaJ1939DA[3]
                spLengthLineaJ1939DA = nuevaLineaJ1939DA[6]
                if (PGNdLineaCanBus == PGNdLineaJ1939DA):
                    analizar=extraexBitsParaAnalizarValidez(trama,spPositionPgLineaJ1939DA,spLengthLineaJ1939DA)
                    resultado1=pasarArrayATexto(nuevaLineaJ1939DA)
                    resultado = " "+analizar+" - "+datosEstanDisponibles(analizar)+" - "+resultado1
                    escribir_nueva_linea_en_fichero_resultados(resultado,ficheroResultados)
                    encontrado = 1
                elif (encontrado == 1):
                    break
                if (m>50000):
                    break
            if (n>3000):
                break
    cerrar_fichero_datos_J1939DA(ficheroJ1939DA)
    cerrar_fichero_datos_CanBus(ficheroCanBus)
    cerrar_fichero_resultados(ficheroResultados)
    print("Fin")

main()
