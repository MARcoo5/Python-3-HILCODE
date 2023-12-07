import random

#defino el constructor de planetas
def constructorPlanetas(nombre,tam, radio, color, x=0, y=0, angulo=0, v_angular=None):
    v_angular = setVelocidad(nombre=nombre)
    objeto = {
            "nombre": nombre,
            "tam": tam,
            "radio": radio,
            "angulo": angulo,
            "v_angular": v_angular,
            "x": x,
            "y": y,
            "color": color,
            "tipo": "planeta"
            }
    return objeto




#########
#########
def setNombre(objeto, nombre):
    if not("nombre" in objeto):
        print("ERROR: El objeto no tiene nombre.")
        return None
    elif not("tipo" in objeto and objeto["tipo"] == "planeta"):
        print("ERROR: El objeto no es de tipo planeta.")
        return None
    elif not(type(nombre) == str):
        print("ERROR: El nombre nuevo no es de tipo string(texto).")
        return None
    else:
        objeto["nombre"] = nombre
        return objeto

def getNombre(objeto):
    return objeto["nombre"]




def setTam(objeto, tam):
    if not("tam" in objeto):
        print("ERROR: El objeto no tiene tamaño.")
        return None
    elif not("tipo" in objeto and objeto["tipo"] == "planeta"):
        print("ERROR: El objeto no es de tipo planeta.")
        return None
    elif not(tam >= 0):
        print("ERROR: El tamaño nuevo tiene que ser mayor que 0.")
        return None
    else:
        objeto["tam"] = tam
        return objeto

def getTam(objeto):
    return objeto["tam"]




def setRadio(objeto, radio):
    if not("radio" in objeto):
        print("ERROR: El objeto no tiene radio.")
        return None
    elif not("tipo" in objeto and objeto["tipo"] == "planeta"):
        print("ERROR: El objeto no es de tipo planeta.")
        return None
    elif not(radio >= 0):
        print("ERROR: El radio nuevo tiene que ser mayor que 0.")
        return None
    else:
        objeto["radio"] = radio
        return objeto

def getRadio(objeto):
    return objeto["radio"]




def setAngulo(objeto, angulo):
    if not("angulo" in objeto):
        print("ERROR: El objeto no tiene ángulo.")
        return None
    elif not("tipo" in objeto and objeto["tipo"] == "planeta"):
        print("ERROR: El objeto no es de tipo planeta.")
        return None
    else:
        objeto["angulo"] = angulo
        return angulo

def getAngulo(objeto):
    return objeto["angulo"]




def setVelocidad(objeto=None, nombre=None):
    velocidad = None
    astros = {
            "sol": 0,
            "mercurio": 0.008,
            "venus": 0.006,
            "tierra": 0.004,
            "marte": 0.002,
            "jupiter": 0.0008,
            "saturno": 0.0006,
            "urano": 0.0004,
            "neptuno": 0.0002
            }
    if nombre != None and nombre in astros and objeto == None:
        velocidad = astros[nombre]
        return velocidad
    elif nombre not in astros and nombre == None:
        velocidad = 0.3/random.randint(1,100)
        return velocidad
    elif "tipo" in objeto and "nombre" in objeto and objeto["tipo"] == "planeta":
        objeto["v_angular"] = velocidad
        return velocidad
    else:
        print("ERROR: Objeto invalido.")
    return objeto

def getVelocidad(objeto):
    if "v_angular" in objeto and "tipo" in objeto and objeto["tipo"] == "planeta":
        return objeto["v_angular"]
    else:
        print("ERROR: Objeto invalido.")




def setX(objeto, x):
    if not("x" in objeto):
        print("ERROR: El objeto no tiene x.")
        return None
    elif not("tipo" in objeto and objeto["tipo"] == "planeta"):
        print("ERROR: El objeto no es de tipo planeta.")
        return None
    elif not(type(x) == int):
        print("ERROR: El x nuevo no es de tipo entero(digitos sin decimales).")
    else:
        objeto["x"] = x
        return x

def getX(objeto):
    return objeto["x"]




def setY(objeto, y):
    if not("y" in objeto):
        print("ERROR: El objeto no tiene y.")
        return None
    elif not("tipo" in objeto and objeto["tipo"] == "planeta"):
        print("ERROR: El objeto no es de tipo planeta.")
        return None
    elif not(type(y) == int):
        print("ERROR: El y nuevo no es de tipo entero(digitos sin decimales).")
    else:
        objeto["y"] = y
        return y

def getY(objeto):
    return objeto["y"]



#
###
#
#
#
#
###!!!!
###TIENE QUE SER: mayor o = a 0 y menor o = a 255
###!!!!
#
#mayor 0, menor 255 & tipo int
#
#
###
#color = f"({colorR},{colorG},{colorB})"
def setColor(objeto,colorR, colorG, colorB):
    if not("color" in objeto):
        print("ERROR: El objeto no tiene color.")
        return None
    elif not("tipo" in objeto and objeto["tipo"] == "planeta"):
        print("ERROR: El objeto no es de tipo planeta.")
        return None
    elif not(type(colorR) == int and type(colorG) == int and type(colorB) == int):
        print("ERROR: Los colores nuevos no son de tipo entero(digitos sin decimales).")
        return None
    elif not(colorR >= 0 and colorR <= 255 and colorG >= 0 and colorG <= 255 and colorB >= 0 and colorB <= 255):
        print("ERROR: Los colores nuevos no estan entre 0 y 255.")
        return None
    else:
        objeto["color"] = (colorR, colorG, colorB)
        return (colorR, colorG, colorB)

def getColor(objeto):
    return objeto["color"]

#########
#########







#creo los planetas:
mercurio = constructorPlanetas(nombre="mercurio", tam=3, radio=50, color=(162,162,162))
venus = constructorPlanetas(nombre="venus", tam=6, radio=100, color=(228,163,98))
tierra = constructorPlanetas(nombre="tierra", tam=10, radio=150, color=(28,156,0))
marte = constructorPlanetas(nombre="marte", tam=12, radio=200, color=(252,34,0))
jupiter = constructorPlanetas(nombre="jupiter", tam=23, radio=250, color=(131,48,21))
saturno = constructorPlanetas(nombre="saturno", tam=18, radio=300, color=(252,200,0))
urano = constructorPlanetas(nombre="urano", tam=15, radio=350, color=(107,217,255))
neptuno = constructorPlanetas(nombre="neptuno", tam=8, radio=400, color=(0,100,255))
PC_test = {"RAM":8, "pantalla":"4K"}

print(getTam(objeto=mercurio))

