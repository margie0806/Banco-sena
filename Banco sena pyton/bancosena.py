class CuentaBancaria:
    def __init__(self, nombre, deposito_inicial):
        self.nombre = nombre
        if deposito_inicial >= 15000:
            self.saldo = deposito_inicial
            print(f"Cuenta creada para {self.nombre} con un depósito inicial de ${self.saldo:.2f}")
        else:
            print("El depósito inicial debe ser igual o superior a $15,000")
            self.saldo = 0
    
    def abonar(self, cantidad):
        self.saldo += cantidad
        print(f"Se abonaron ${cantidad:.2f} a la cuenta. Saldo total: ${self.saldo:.2f}")
    
    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.nombre} es: ${self.saldo:.2f}")
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se retiraron ${cantidad:.2f} de la cuenta. Saldo restante: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes para realizar el retiro.")

# Función principal del programa
def main():
    nombre = input("Ingrese el nombre del afiliado: ")
    deposito_inicial = float(input("Ingrese el monto del depósito inicial: "))
    
    cuenta = CuentaBancaria(nombre, deposito_inicial)
    
    while True:
        print("\nMenú de opciones:")
        print("1. Abonar a la cuenta")
        print("2. Mostrar saldo")
        print("3. Retirar")
        print("4. Salir")
        
        opcion = input("Ingrese el número de la opción que desea realizar: ")
        
        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad a abonar: "))
            cuenta.abonar(cantidad)
        elif opcion == '2':
            cuenta.mostrar_saldo()
        elif opcion == '3':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == '4':
            print("Gracias por utilizar nuestros servicios. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()
