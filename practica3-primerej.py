class Calculadora:
    """
    Calculadora.

    Atributos
    ---------
    v1:
        Primer operando
    v2:
        Segundo operando

    Metodos:
    -------
    Sumar:
        Suma los operandos v1 y v2
    Restar:
        Resta los operandos v1 y v2
    Producto:
        Multiplica los valores de v1 y v2 entre si
    Division:
        Divide los valores de v1 y v2 entre si
    Primo:
        Comprueba que el operando v1 sea primo

    EJEMPLO:
    -------
    >>> import Calculadora
    >>> a = Calculadora(3,9)
    >>> resultado = calculadora.multiplicar()
    """

    def __init__(self,v1,v2):
        assert(isinstance(v1, int) and isinstance(v2, int))
        self.v1 = float(v1)
        self.v2 = float(v2)


    def sumar(self):
        """
        Suma los operandos v1 y v2
        """
        suma = self.v1+self.v2
        return suma

    def restar(self):
        """
        Resta los operandos v1 y v2
        """
        resta = self.v1-self.v2
        return resta

    def multiplicar(self):
        """
        Multiplica los operandos v1 y v2
        """
        multiplicar = self.v1*self.v2
        return multiplicar


    def dividir(self):
        """
        Divide los operandos v1 y v2
        """
        dividir = self.v1/self.v2
        return dividir
