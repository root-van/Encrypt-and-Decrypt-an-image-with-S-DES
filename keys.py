import random 
orden1 = [2,6,3,1,4,8,5,7]
orden2 = [4,1,2,3,2,3,4,1]
tipo1 = []
tipo2 = []
# Author: rootvan

# llaves tipo 1
def llaves_tipo1():
        for i in range(1500):
            x=[]
            K0=[]
            K1=[]
            
            # se generan las keys
            for y in range(10):
                n = random.randint(0, 1)
                x.append(str(n))
            
            for y in range(8):
                K0.append(x[orden1[y]])

            for y in range(8):
                K1.append(x[orden2[y]])

            if(K0 == K1):
                tipo1.append(x)
            else:
                pass
                        
        with open ('tipo1.txt','w') as f:
            for i in range(len(tipo1)):
                f.write(str(tipo1[i])+str("\n"))
        f.close()
        print("se ha generado tipo1.txt")

# llaves tipo 2
def llaves_tipo2():
        for i in range(50000):
            x=[]
            K0=[]
            K1=[]
            Kprima=[]
            K0_prima=[]
            K1_prima=[]

            for y in range(10):
                n = random.randint(0, 1)
                x.append(str(n))

            for y in range(10):
                n = random.randint(0, 1)
                Kprima.append(str(n))
            
            # k0
            for y in range(8):
                n = orden1[y]
                K0.append(x[n])

            # k1
            for y in range(8):
                n=orden2[y]
                K1.append(x[n])

            # k0prima
            for y in range(8):
                n=orden1[y]
                K0_prima.append(Kprima[n])

            # k1prima
            for y in range(8):
                y=orden2[y]
                K1_prima.append(Kprima[n])

            if K0==K1_prima:
                if K1==K0_prima:
                    tipo2.append(x)
                    tipo2.append(Kprima)
                else:
                    pass
            else:
                pass


        with open ('tipo2.txt','w') as file:
            for i in range(len(tipo2)):
                file.write(str(tipo2[i])+str("\n"))
        file.close()
        print("se ha generado tipo2.txt")

def main():
        llaves_tipo1()
        llaves_tipo2()
