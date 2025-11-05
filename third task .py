def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter The Num "))

if prime_num(num):
    print(f"{num} -->  Is Prime Number ")
else:
    print(f"{num} --> Is Not Prime Number ")