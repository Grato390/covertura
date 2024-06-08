class Calculadora:
    # Sumar dos números
    def sumar(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Ambos argumentos deben ser números.")
        return a + b

    # Restar dos números
    def restar(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Ambos argumentos deben ser números.")
        return a - b

# Ejemplo de uso de la clase Calculadora
try:
    calculadora = Calculadora()

    # Sumar dos números
    print("Suma de 5 y 3:", calculadora.sumar(5, 3))

    # Restar dos números
    print("Resta de 5 y 3:", calculadora.restar(5, 3))

    # Intentar sumar con un argumento no numérico
    print("Suma de 5 y 'a':", calculadora.sumar(5, 'a'))

except ValueError as e:
    print("Error:", e)
