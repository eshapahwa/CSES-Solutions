n = int(input())

sequence = []

while n != 1:
    sequence.append(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
sequence.append(1)

print(" ".join(map(str, sequence)))