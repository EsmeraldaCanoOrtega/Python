class Persona:
    contador_personas = 0

#   1º manera más recomendada para cambiar un atributo estatico y devolver el valor
    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas


    def __init__(self, nombre, edad):
#   2º manera sería     Persona.contador_personas +=1
#                       self.id_persona= Persona.contador_personas

        self.id_persona = Persona._generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'
#   1 persona
persona1 = Persona('Juan', 28)
print(persona1)
#   2 persona
persona2 = Persona('Karla', 30)
print(persona2)
#   3 persona
persona3 = Persona('Eduardo', 25)
print(persona3)
print(f'Valor contador personas: {Persona.contador_personas}')