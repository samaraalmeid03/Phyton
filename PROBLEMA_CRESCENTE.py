x: int
y: int

print("Digite dois numeros:")
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print("CRESCENTE!")
    else:
        print("DECRESCENTE!")

    print("Digite outrso dois numeros:")
    x = int(input())
    y = int(input())