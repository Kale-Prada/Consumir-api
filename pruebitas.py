lista = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

lista_diccionario=[] #es una lista de diccionarios. No es un diccionario entero. 
num=0
for i in lista: 
    #print(i)
    num = num + 1
    #append se usa en listas para agregar algo a cada elemento de la lista 
    #agregar un diccionario por cada vuelta a mi lista
    lista_diccionario.append({"clave":num, "valor":i}) #agregar un diccionario por cada vuelta a mi lista 
    print(lista_diccionario)

    for diccionario in lista_diccionario:
        print(f"{diccionario['clave']} - {diccionario['valor']}")

seleccion = input("Seleccione un numero para categoria: ") 
int (seleccion)
for diccionario in lista_diccionario:
    if diccionario['clave'] == int(seleccion):
        print(f"tu seleccion fue {diccionario['valor']}")
        