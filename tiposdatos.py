print(" Clases V2 Sebastian Rojas ")

# zona de clase
class Datos:

    def __init__(self, estatura, peso):
        self.estatura=estatura
        self.peso=peso

    def mostrar_datos(self):
        print(f"Estatura : {self.estatura} mts, peso {self.peso} Kg")

    def mi_lista(self):
        Aeropuertos=["Abraham Gonzales (CJS)","AIFA (CDMX)","AICM (CDMX)"]
        print(Aeropuertos)
        for aer in Aeropuertos:
            print(aer)

    def mi_tupla(self):
        Ciudades=("Ciudad de Mexico","Ciudad Juarez","Cancun")
        print(Ciudades)
        for ciu in Ciudades:
            print(ciu)

    def mi_conjunto(self):
        estados={"Estado de Mexico","Chihuahua","Quintana Roo"}
        print(estados)
        for est in estados:
            print(est)
    def mi_diccionario(self):
        thisdict = {
        "Partida": "Ciudad Juarez, Chihuahua",
        "Destino": "Cancun, Quintana Roo",
        "Fecha y Hora": 18.30
    }
        print(thisdict)
        for x, y in thisdict.items():
            print(x, y)
        
info=Datos(1.73,55)

info.mostrar_datos()
print("LISTA DE AEROPUERTOS")
print("")
info.mi_lista()
print("")
print("")
print("Tupla DE Ciudades")
print("")
info.mi_tupla()
print("")
print("")
print("Conjunto DE Estados")
print("")
info.mi_conjunto()
print("")
print("")
print("Diccionario DE Boleto")
print("")
info.mi_diccionario()
