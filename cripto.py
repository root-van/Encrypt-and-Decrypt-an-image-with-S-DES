import base64
import random
import desencriptar
import keys
# Author: rootvan

# generate key 10 bits
def generate_keys():
        key = []
        for i in range(10):
                n = random.randint(0, 1)
                key.append(str(n))

        # define order of p10
        orden = [3,5,2,7,4,10,1,9,8,6]
        p10 = []
        # generate p10
        for i in orden:
                n = key[i-1]
                p10.append(str(n))

        # lL y lR listas
        lL = []
        lR = []

        # split p10 & create lL
        for i in range(0,5):
                lL.append(p10[i])

        # split p10 & create lR
        for i in range(5, len(p10)):
                lR.append(p10[i])

        #
        # left shift one position lL & lR
        lL = lL[1:]+lL[:1]
        lR = lR[1:]+lR[:1]
        lsi = []
        #

        # unimos los dos lados ya 
        # con el desplazamiento
        for i in lL:
                lsi.append(i)
        for i in lR:
                lsi.append(i)
        #
        # define order of p8
        p8 = [6,3,7,4,8,5,10,9]
        k1 = []
        for i in p8:
                n = lsi[i-1]
                k1.append(n)
        print("\n============= Llaves generadas! ============= ")
        print(f"k1 = {k1}")
        # guardar k1 en un archivo txt
        archivo = open("k1.txt","w")
        archivo.write(str(k1))
        archivo.close()

        lL = []
        lR = []
        # split lsi & create lL
        for i in range(0,5):
                lL.append(lsi[i])

        # split lsi & create lR
        for i in range(5, len(lsi)):
                lR.append(lsi[i])

        # left shift two positions lL & lR
        lL = lL[2:]+lL[:2]
        lR = lR[2:]+lR[:2]
        lsi = []
        k2 = []
        #
        # ls0 + ls1 = k2
        for i in range(5):
                lsi.append(lL[i])
        for i in range(5):
                lsi.append(lR[i])

        # obtenemos k2
        for i in p8:
                n = lsi[i-i]
                k2.append(n)
        print(f"k2 = {k2}")
        # guardar k2 en un archivo txt
        archivo = open("k2.txt","w")
        archivo.write(str(k2))
        archivo.close()
        print("============= Llaves generadas! ============= \n")

def encriptar(cadena,key1,key2):
    k1 = key1
    k2 = key2
    # ============== segunda parte encriptacion ==================================
    m = cadena
    PT = []

    # añadimos los valores obtenidos de cadena a PT
    for i in range(8):
        n = m[i] 
        PT.append(n)

    # convertimos los elemntos de la lista a enteros
    PT = [int(x) for x in PT]
    IP = [2,6,3,1,4,8,5,7]
    AfterIP = []

    # aplicamos la permutacion inicial
    for i in IP:
        n = PT[i-1]
        AfterIP.append(n)

    # segmentamos en dos
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
    #k = [1,0,1,0,0,1,0,0]
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
    #k = [0,1,0,0,0,0,1,1]
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

    IPi = [4,1,3,5,7,2,8,6]
    c = []
    for i in IPi:
        n = p4[i-1]
        c.append(n)
    return c

if __name__ == "__main__":
    while True:
        opc = int(input("----- S-DES MENU DE OPCIONES -----\n[1]Generar keys [2]Encriptar [3]Desencriptar [4]keys vulnerables [5]Salir\n\nseleccione una opcion -> "))
        if opc == 1:
            generate_keys()
        elif opc == 2:
            k1 = "k1.txt"
            k2 = "k2.txt"

            # se lee la key 1
            archivo = open(k1)
            k1 = archivo.read()
            archivo.close()

            # se lee la key 2
            archivo = open(k2)
            k2 = archivo.read()
            archivo.close()

            print ("------Encriptar------")
            # convertiremos la imagen a lista
            m = []
            imagen = []
            crip = []

            # se lee en modo binario
            e = base64.b64encode(open("imagen.jpg","rb").read()).decode()
            
            # se le da formato ascii
            a_bytes = bytes(e, "ascii")

            # se le da formato binario
            for i in a_bytes:
                    m.append(format(i,'08b'))

            text_cip = []


            # segmentamos en listas de 8 bits para ir encriptando
            for i in range(len(m)):   
                if len(str(m[i]))==8:
                    text_cip.append(encriptar(str(m[i]),k1,k2))

            # lo convertimos en una sola lista con n bits
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

            txt=""

            # eliminamos el formato de lista
            for u in texto:
                txt+=u+" "

            # guardamos imagen
            nombre_imagen = input("Ingrese el nombre o la ruta de la imagen: ")
            with open(nombre_imagen,"wb") as file:
                cifrado = bytes(txt,"ascii")
                file.write(cifrado)
                file.close()
            print("*Se encripto la imagen correctamente")
        elif opc == 3:
            desencriptar.main()
        elif opc == 4:
            keys.main()
        elif opc == 5:
            break
        else:
            print("Error! Ingrese una opcion valida")
