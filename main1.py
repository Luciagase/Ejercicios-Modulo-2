#1) Utiliza el metodo input()
#1.A
resultado=input('Escribe un numero: ') #Al utilizar el método input, el programa espera a que el usuario introduzca un valor en el teclado. Si no lo introduces el programa no termina de leer el código. Para guiar al usuario se puede escribir una instrución entre los paréntesis del input que informará de que se necesita introducir un un valor.
print(resultado)
print(type(resultado))

#1.B
Num=int(input('Escribe un numero diferente:')) #El número en input es de por sí una string, por lo que si no utilizamos una función int o float no podremos realizar operaciones con ese número. La diferencia entre int y float es que int transforma la variable en un entero y float en un número flotante.
print(Num)
print(type(Num))

#1.C
num=float(input('Escribe otro numero:'))
print(num)
print(type(num))


