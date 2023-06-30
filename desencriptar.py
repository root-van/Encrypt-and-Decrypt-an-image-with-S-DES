import base64
from unicodedata import name
# Author: rootvan


def convertir_base64(x):
    asc = ""
    #Convertimos a int la lista
    for valor in x:
        entero = int(valor, 2)
    #Convertimos a la base 2 en un entero decimal
        ascii_char = chr(entero)
    #Convertimos a Ascii el decimal
        asc += ascii_char
    #Append character to `ascii_string`
    return asc

def desencriptar(cadena,key1,key2):
    k1 = key1
    k2 = key2
    k1 = [0, 0, 1, 0, 0, 1, 1, 0]
    k2 = [0, 0, 0, 0, 0, 0, 0, 0]
    m = cadena
    c = []

    for i in range(8):
        n = m[i] 
        c.append(n)
    c = [int(x) for x in c]
    IP = [2,6,3,1,4,8,5,7]
    AfterIP = []
    for i in IP:
        n = c[i-1]
        AfterIP.append(n)

    L = []
    for i in range(4):
        n = AfterIP[i]
        L.append(n)

    R = []
    for i in range(4,len(AfterIP)):
        n = AfterIP[i]
        R.append(n)

    ep = [4,1,2,3,2,3,4,1]
    Aftep = []
    for i in ep:
        n = R[i-1]
        Aftep.append(n)

    sk = []
    # funcion X0R
    for i in range(8):
        if Aftep[i] == 0:
            if k2[i] == 0:
                sk.append(0)
            else:
                sk.append(1)
        else:
            if k2[i] == 0:
                sk.append(1)
            else:
                sk.append(0)

    # s-boxs
    s0 = [['01','00','11','10'],
          ['11','10','01','00'],
          ['00','10','01','11'],
          ['11','01','11','10']]

    s1 = [['00','01','10','11'],
          ['10','00','01','11'],
          ['11','00','01','00'],
          ['10','01','00','11']]

    x0 = []
    x1 = []

    #segmentamos sk en dos partes
    for i in range(4):
        x0.append(sk[i])

    for i in range(4,8):
        x1.append(sk[i])

    # tomamos el primer valor de x0 y el ultimo
    s0row = str(x0[0]) + str(x0[3])
    s0column = str(x0[1]) + str(x0[2])


    # tomamos el primer valor de x1 y el ultimo
    s1row = str(x1[0]) + str(x1[3])
    s1column = str(x1[1]) + str(x1[2])

    if s0row == "00":
        s0row = 0
    elif s0row == "01":
        s0row = 1
    elif s0row =="10":
        s0row = 2
    elif s0row == "11":
        s0row = 3

    if s1row == "00":
        s1row = 0
    elif s1row == "01":
        s1row = 1
    elif s1row == "10":
        s1row = 2
    elif s1row == "11":
        s1row = 3

    if s0column == "00":
        s0column = 0
    elif s0column == "01":
        s0column = 1
    elif s0column == "10":
        s0column = 2
    elif s0column == "11":
        s0column = 3

    if s1column == "00":
        s1column = 0
    elif s1column == "01":
        s1column = 1
    elif s1column == "10":
        s1column = 2
    elif s1column == "11":
        s1column = 3

    s0s1 = str(s0[s0row][s0column])+str(s1[s1row][s1column])
    orden = [2,4,3,1]
    p4 = []
    # funcion XOR
    for i in range(4):
        if s0s1[i] == 0:
            if L[i] == 0:
                p4.append(0)
            else:
                p4.append(1)
        else:
            if L[i] == 0:
                p4.append(1)
            else:
                p4.append(0)

    for i in range(4):
        p4.append(R[i])

    p4 = p4[4:]+p4[:4]

    # ========= round 2 ==============================================
    L = []
    for i in range(4):
        n = p4[i]
        L.append(n)

    R = []
    for i in range(4,len(AfterIP)):
        n = p4[i]
        R.append(n)


    ep = [4,1,2,3,2,3,4,1]
    Aftep = []
    for i in ep:
        n = R[i-1]
        Aftep.append(n)

    sk = []
    # funcion X0R
    for i in range(8):
        if Aftep[i] == 0:
            if k1[i] == 0:
                sk.append(0)
            else:
                sk.append(1)
        else:
            if k1[i] == 0:
                sk.append(1)
            else:
                sk.append(0)

    # s-boxs
    s0 = [['01','00','11','10'],
          ['11','10','01','00'],
          ['00','10','01','11'],
          ['11','01','11','10']]

    s1 = [['00','01','10','11'],
          ['10','00','01','11'],
          ['11','00','01','00'],
          ['10','01','00','11']]

    x0 = []
    x1 = []

    #segmentamos sk en dos partes
    for i in range(4):
        x0.append(sk[i])

    for i in range(4,8):
        x1.append(sk[i])

    # tomamos el primer valor de x0 y el ultimo
    s0row = str(x0[0]) + str(x0[3])
    s0column = str(x0[1]) + str(x0[2])


    # tomamos el primer valor de x1 y el ultimo
    s1row = str(x1[0]) + str(x1[3])
    s1column = str(x1[1]) + str(x1[2])

    if s0row == "00":
        s0row = 0
    elif s0row == "01":
        s0row = 1
    elif s0row =="10":
        s0row = 2
    elif s0row == "11":
        s0row = 3

    if s1row == "00":
        s1row = 0
    elif s1row == "01":
        s1row = 1
    elif s1row == "10":
        s1row = 2
    elif s1row == "11":
        s1row = 3

    if s0column == "00":
        s0column = 0
    elif s0column == "01":
        s0column = 1
    elif s0column == "10":
        s0column = 2
    elif s0column == "11":
        s0column = 3

    if s1column == "00":
        s1column = 0
    elif s1column == "01":
        s1column = 1
    elif s1column == "10":
        s1column = 2
    elif s1column == "11":
        s1column = 3

    s0s1 = str(s0[s0row][s0column])+str(s1[s1row][s1column])
    orden = [2,4,3,1]
    p4 = []
    # funcion XOR
    for i in range(4):
        if s0s1[i] == 0:
            if L[i] == 0:
                p4.append(0)
            else:
                p4.append(1)
        else:
            if L[i] == 0:
                p4.append(1)
            else:
                p4.append(0)

    for i in range(4):
        p4.append(R[i])

    IPi = [4,1,3,5,7,2,8,6]
    pt = []
    for i in IPi:
        n = p4[i-1]
        pt.append(n)
    return pt

def main():
    print ("------Desencriptar------")
    k1 = str(input("ingresa k1: "))
    k2 = str(input("ingresa k2: "))
    # se lee la key 1
    archivo = open(k1)
    k1 = archivo.read()
    archivo.close()

    # se lee la key 2
    archivo = open(k2)
    k2 = archivo.read()
    archivo.close()
    
    m=[]
    crip=[]
    # Convertimos la imagen en una lista de bits 
    datos = open("imagen_encriptada.jpg","rb").read().decode()
    datos2 = ""
    for i in range(0,(len(datos)-1)):
        datos2 += datos[i] 
    m=datos2.split()

    #Realizamos el proceso de encriptar y lo guardaremos en la lista text_cip
    text_cip=[]

    # segmentamos en listas de 8 bits para ir desencriptando
    for i in range(len(m)):   
        if len(str(m[i]))==8:
            text_cip.append(desencriptar(str(m[i]),k1,k2))

    # lo convertimos en una sola lista de n bits
    for n in range(len(text_cip)):
        for j in range(8):
            crip.append(text_cip[n][j])
    texto=[]
    txt=""

     # agrupamos 8 bits para cada indice de la lista
    for i in range(len(crip)):
        txt = txt + str(crip[i])
        if len(txt)==8:
            texto.append(str(txt))
            txt=""
    imagen = base64.b64decode(convertir_base64(texto))
    with open("imagen_desencriptada.jpg","wb") as file:
        file.write(imagen)
        file.close()
    #print(texto)
    print("*Se desencripto la imagen correctamente")


