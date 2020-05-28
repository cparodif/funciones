def calcularCanId(p):
    x = "0"+p[:-1]
    x = x[-8:]
    return x

def calcularTrama(p):
    trama = p[2:25]
    return trama

def calcularTramab(p):
    x=hexadecimalEnBinario(calcularTrama(p))
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

