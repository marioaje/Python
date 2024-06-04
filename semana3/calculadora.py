# funcion de suma

# funcion de resta

class calculadora:
    def __int__(self):
        self.resultado = 0.0

    def suma(self, valor1):
        self.resultado += valor1

    def retornarresultado(self):    
        return self.resultado

nuevavariable = calculadora()  
capturavalor1 = 3
capturavalor2 = 9
nuevavariable.suma( capturavalor1, capturavalor2 )
nuevavariable.resultado