from flask import Flask, jsonify
import random
app = Flask (__name__)
'''
CONTADOR DE ID AUTOINCREMENTABLES
'''
count_id=1
name = ["Sofía", "Mateo", "Valentina", "Sebastián", "Isabella", "Alejandro", "Camila", "Daniel", "Martina", "Nicolás"]
lastname = ["García", "Rodríguez", "López", "Martínez", "Pérez", "González", "Sánchez", "Fernández", "Ruiz", "Díaz"]
people= []
#GENERADOR DE NUMERO DE IDENTIFICACION
def generate_identification_random(length):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return ''.join(str(random.choice(digits)) for i in range(length))
'''
Va recorriendo la lista de digist que son los digitos que puede tener y captura uno aleatoriamente 
y lo almacena en la lista hasta completar el numero de digitos que le soliciten
'''
#CICLO PARA LLENAR LA LISTA DE LAS PERSONAS CON SU INFORMACION
for i in range (len(name)):
    new_people = {
        'id': count_id,
        'name': name[i], # Esto toma la posicion de cada intervalo que se vaya ejecutando
        'last_name':lastname[i],# Esto toma la posicion de cada intervalo que se vaya ejecutando
        'identification_number': generate_identification_random(10)  # Solicita un numero aleatorio a la funcion generadora de identificacion
    }
    people.append(new_people)
    count_id += 1 #incrementador de id de usuario
    
@app.route('/personas')
def get_all_personas():
    return jsonify({"list_people":people})
'''
list_people es el titulo que va antes de la lista que se convertira en json esto se utiliza
para idenfitificar un json si tienes mas de uno en el mismo codigo
'''

if __name__ == '__main__':
    app.run(debug=True)
