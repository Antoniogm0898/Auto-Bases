
#!/usr/bin/python
import pandas as pd
from random import randint

def generateADFy3B():
    rng = 5000
    cc = ["3 BBB", "ADF"]
    reg = ["Centro", "Noroeste", "Sur"]
    gz = ["Cd. Mx", "Baja California", "San Luis", "Chihuahua", "Nayarit"]
    brn = ["Marca1", "Marca2", "Marca3", "Marca4", "Marca5"]
    le = ["Pr1", "Pr2", "Pr3", "Pr4", "Pr5"]
    seg = ["Alto", "Bajo", "Promedio", "Premium"]
    est = ["Estilo1", "Estilo2", "Estilo3", "Estilo4"]
    pre = ["Presentacion1", "Presentacion2", "Presentacion3", "Presentacion4", "Presentacion5"]
    mul = ["Empaque1", "Empaque2", "Empaque3", "Empaque4", "Empaque5"]
    flag = True
    clienteCadena = []
    region = []
    gzz = []
    marca = []
    lineextension = []
    segment = []
    estilo = []
    presentacion = []
    multipacks = []
    en20 = []
    fe20 = []
    ma20 = []
    en21 = []
    fe21 = []
    ma21 = []
    for x in range(rng):
        clienteCadena.append(cc[randint(0, 1)])
        region.append(reg[randint(0, 2)])
        gzz.append(gz[randint(0, 4)])
        marca.append(brn[randint(0, 4)])
        lineextension.append(le[randint(0, 4)])
        segment.append(seg[randint(0, 3)])
        estilo.append(est[randint(0, 3)])
        presentacion.append(pre[randint(0, 4)])
        multipacks.append(mul[randint(0, 4)])
        en20.append(randint(0, 2000))
        fe20.append(randint(0, 2000))
        ma20.append(randint(0, 2000))
        en21.append(randint(0, 2000))
        fe21.append(randint(0, 2000))
        ma21.append(randint(0, 2000))
        
    data = [clienteCadena, region, gzz, marca, lineextension, segment, estilo, presentacion, multipacks, en21, fe21, ma21, en20, fe20, ma20]
    names = ["Cliente Cadena", "Region", "GZ", "Brand", "Line Extension", "Segment", "Styles", "Presentación CMM", "Multipacks", "Enero 21", "Febrero 21", "Marzo 21", "Enero 20", "Febrero 20", "Marzo 20"]
    df = pd.DataFrame(data, names).T
    df.to_excel("../Input/InputADF&3B.xlsx", index = False)

def run():
    generateADFy3B()
