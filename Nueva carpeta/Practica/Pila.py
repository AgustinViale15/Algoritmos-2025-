from random import randint

from stack import Stack

Number_stack = Stack()
Pares = Stack()
Impares = Stack()

for i in range (5):                     #hace un for para llenar la pila
    rand_number = randint(1,100)
    print(rand_number)
    Number_stack.push(rand_number)      #apila

while Number_stack.size() > 0:      #separa en pares e impares
    Number = Number_stack.pop()
    if Number % 2 == 0:
        Pares.push(Number)
    else:
        Impares.push(Number)

Pares.show()
Impares.show()