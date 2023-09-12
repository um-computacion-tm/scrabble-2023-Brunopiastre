class Dictionary:
     
    def __init__(self, dictionary = "diccionario.txt" ):
        self.dictionary = dictionary


with open('diccionario.txt', 'r') as archivo:
    contenido = archivo.read()
    
print(contenido)




       'COMO HAGO PARA QUE LEA LAS PALABRAS DEL ARCHIVO DICCIONARIO'

    def diccionario(diccionario.txt):
        try:
            with open(diccionario.txt, 'r') as archivo:
                palabras = archivo.read().splitlines()
            return palabras
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return []
    