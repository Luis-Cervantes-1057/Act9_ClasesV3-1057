print("Actividad 9 Clase Humano")
print("Luis Cesar Cervantes Velazquez: 22308051281057")
# Zona de Class

class Humano1057:
    # Zona de atributos
    edad = 0
    nombre = "Luis Cesar"
    ape = "Cervantes Velazquez"
    fenac = "3 de Marzo del 2007"
    apodo = "Wicho"
    fav = "Como BAQUIAT Jhayco"


    # Zona de funciones
    def correr1057(self, n):
        print(f"{n} esta corriendo ufff...")
    def Jugar1057(self, n):
        print(f"{n} juega fucho")
    def platicar1057(self, n):
        print(f"{n} esta platicando")
    def escucha1057 (self,n,nn):
        print(f"{n} escucha a {nn}")
    def dormir1057(self, n):
        print(f"{n} duerme machin")

# Zona de Creacion de objeto
luis = Humano1057()
ale = Humano1057()

# Zona Usando objetos
print("Reusltados para Luis")
luis.edad = 17
luis.nombre
luis.ape
luis.fenac
luis.apodo
luis.fav
print(f"Edad: {luis.edad}")
print(f"Nombre: {luis.nombre}")
print(f"Apellidos: {luis.ape}")
print(f"Fecha de Nacimiento: {luis.fenac}")
print(f"Apodo: {luis.apodo}")
print(f"Cancion Favorita: {luis.fav}")

luis.correr1057("Luis")
luis.Jugar1057("Luis")
luis.platicar1057("Luis")
luis.escucha1057("Luis", "Ivan Cornejo")
luis.dormir1057("Luis")

print(" ")
print("Resultado para Alesita")
ale.edad = 18
ale.nombre=" Mia ALejandra"
ale.ape = "Alcantar"
ale.fenac = "6 de Julio del 2006"
ale.apodo = "Alesita"
ale.fav = "Hasta La Muerte"
print(f"Edad: {ale.edad}")
print(f"Nombre: {ale.nombre}")
print(f"Apellidos: {ale.ape}")
print(f"Fecha de Nacimiento: {ale.fenac}")
print(f"Apodo: {ale.apodo}")
print(f"Cancion Favorita: {ale.fav}")

luis.correr1057("Ale")
luis.Jugar1057("Ale")
luis.platicar1057("Ale")
luis.escucha1057("Ale", "Fuerza Regida")
luis.dormir1057("Ale")
