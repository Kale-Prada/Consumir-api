import requests as consulta 
#https://api.chucknorris.io/jokes/categories
categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
print("categorias: ",categorias.json())

lista_categoria =categorias.json()
lista_categoria_dic = []
num=0
for i in lista: 
    #print(i)
    num = num + 1
    #append se usa en listas para agregar algo a cada elemento de la lista 
    #agregar un diccionario por cada vuelta a mi lista
    lista_diccionario.append({"clave":num, "valor":i}) #agregar un diccionario por cada vuelta a mi lista 
    print(lista_diccionario)

    seleccion = input("Seleccione un número para categoría: ")

    for diccionario in lista_diccionario:
        print(f"{diccionario['clave']} - {diccionario['valor']}")   
        



print("último dato de lista categoria: ",lista_categoria[len(lista_categoria)-1])
response = consulta.get('https://api.chucknorris.io/jokes/random?category=animal')

print("código http de respuesta: ",response.status_code)
print("cabecera: ",response.headers['content-type'])
print("enconding: ",response.encoding)
print("respuesta en string: ",response.text)
print("respuesta en json: ",response.json())

