n = int(input())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:
    even_numbers = list(range(2, n + 1, 2))
    odd_numbers = list(range(1, n + 1, 2))
    beautiful_permutation = even_numbers + odd_numbers
    print(" ".join(map(str, beautiful_permutation)))
