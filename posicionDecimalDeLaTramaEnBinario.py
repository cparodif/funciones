def posicionDecimalDeLaTramaEnBinario(pTramah, pPosicion, pLongitud):
# posicionDecimalDeLaTramaEnBinario("00 00 00 0c 06 54 23 41", "1.3", "2 bits"):    
    # posicion "1.3" o "2-3"
    numCaracteres = len(pPosicion)
    if (numCaracteres == 1):
        x = pPosicion
    if (numCaracteres == 2):
        x = pPosicion
    if (numCaracteres == 3):
        if (pPosicion[1] == "."):
            x= ((int(pPsicion[0])-1)*8)+int(pPsicion[1])-1
            
        if (pPosicion[1] == "-"):
            #inluir los dos bytes, de la trama pero en orden inverso
            x = pPosicion

    if (pLongitud == "1 bit")
         y = 1
    if (pLongitud == "2 bits")
         y = 2
    if (pLongitud == "3 bits")
         y = 3
    if (pLongitud == "4 bits")
         y = 4
    if (pLongitud == "5 bits")
        y = 5
    if (pLongitud == "6 bits")
        y = 6
    if (pLongitud == "7 bits")
        y = 7
    if (pLongitud == "8 bits")
        y = 8
    if (pLongitud == "9 bits")
        y = 9
    if (pLongitud == "10 bits")
        y = 10
    if (pLongitud == "1 byte")
        y = 8
    if (pLongitud == "2 bytes")
        y = 16
    if (pLongitud == "3 bytes")
        y = 24
    if (pLongitud == "4 bytes")
        y = 32
    
    datosParaAnalizar = pTrama[x:y]
    
    return datosParaAnalizar


    

def datosEstanDisponibles():
