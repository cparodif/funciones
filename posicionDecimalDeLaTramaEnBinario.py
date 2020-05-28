def numeroDeBits():
    y=0
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
    return y

def posicionDecimalDeLaTramaEnBinario(pTramah, pPosicion, pLongitud):
# posicionDecimalDeLaTramaEnBinario("00 00 00 0c 06 54 23 41", "1.3", "2 bits"):
    pTramah.strip()
    pTrama = pTramah.split(" ")
    y = numeroDeBits(pLongitud)
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
        x = pPosicion[0]
        datosParaAnalizar = hexadecimalEnBinario(pTrama[int(pPosicion[0])])

    if (numCaracteres == 3):
        if (pPosicion[1] == "."):
            x= ((int(pPsicion[0])-1)*8)+int(pPsicion[2])-1
            datosParaAnalizar = hexadecimalEnBinario(pTrama[int(pPosicion[0])])

        if (pPosicion[1] == "-"):
            #inluir los dos bytes, de la trama pero en orden inverso
            x1 = int(pPosicion[0])-1
            x2 = int(pPosicion[2])-1
            datosParaAnalizar = hexadecimalEnBinario(x2)+hexadecimalEnBinario(x1)

    return datosParaAnalizar


def datosEstanDisponibles():
