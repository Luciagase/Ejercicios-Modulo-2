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
num=float(input('Escribe otro numero: '))
print(num)
print(type(num))

#2) Vamos a formatear números:

#2.A
num_2=int(input('Escribe un numero (para enteros): '))

#2.B
print("{:05d}".format(num_2))

#2.C
num_3=float(input('Escribe un numero (para flotantes): '))

#2.D
print("{:09.3f}".format(num_3))

#3) Vamos a ponernos creativos. ¿Cuántas formas tienes de mostrar esta información?La altura es de 1,80 metros y el peso es de 80,135 KG

altura=float(input('Elije una unidad  '))
peso=float(input('Peso en kg: '))

print()