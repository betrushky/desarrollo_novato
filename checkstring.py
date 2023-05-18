"""
Script analizador de cadenas; El ususario ingresa un texto, sin importar el tamaño del mismo.
El script le solicita tres letras adicionales que utilizara en la busqueda de dichas letras dentro de la cadena de texto que se ingreso previamente
"""
texto = input('Ingresa el texto a analizar: ')
mi_listas= [input('Escribe una letra: ').lower(),input('Escribe una letra: ').lower(),input('Escribe una letra: ').lower()]
"""
Se pasa el texto introducido por el usuario a letras minusculas para estandarizarlo.
"""
texto = texto.lower()
"""
Se analizan las letras que coincidan con el texto y se cuenta las veces que aparecen en el mismo
"""
print(f"La letra {mi_listas[0]} aparece {texto.count(mi_listas[0])} veces en tu texto")
print(f"La letra {mi_listas[1]} aparece {texto.count(mi_listas[1])} veces en tu texto")
print(f"La letra {mi_listas[2]} aparece {texto.count(mi_listas[2])} veces en tu texto")
"""
El texto se agrega a una lista separada con el espacio.
"""
text_list = texto.split()
"""
Se cuentan los elementos de la lista que seran coincidientes con el numero de palabras que existen en el texto.
"""
print(f"Existen {len(text_list)} palabras en tu texto")
"""
Se muestra en pantalla tanto la primera como la ultima letra que aparece en el texto.
"""
print(f"La primera letra en tu texto es \"{texto[0]}\"")
print(f"La ultima letra en tu texto es \"{texto[-1]}\"")
"""
Se muestra el texto al revez 
"""
print(f"{texto[::-1]}")
"""
Como en estos momentos se desconoce el uso de condicionales, se procedio a hacer una evaluacion por medio de un diccionario si es que la palabra
python se encuentra dentro del texto que ingreso el usuario
"""
respuesta = 'python' in text_list
respuestas_dic={'True':'Si','False':'No'}
print(f"la palabra python {respuestas_dic[str(respuesta)]} se encuentra en el texto")

"""
Como accion adicional se requiere que los metodos aplicados en el codigo se ingresen dentro de una o varias funciones y que se agrege otro metodo
adicional que muestre el texto ingresado en pantalla en letras mayusculas y que se analice si es que el texto contiene caracteres especiales (*,+,%,&) dentro del mismo texto.
"""
