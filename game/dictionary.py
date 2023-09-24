class Dictionary:
     
    def __init__(self, dictionary = "diccionario.txt" ):
        self.dictionary = dictionary


with open('diccionario.txt') as archivo:
    contenido = archivo.read()
    
print(contenido)


def diccionario(contenido):
    try:
        with open('diccionario.txt', 'r') as archivo:
            palabras = archivo.read().splitlines()
        return palabras
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return []