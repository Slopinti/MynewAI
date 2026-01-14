def sentence():
    sentence = input("entera sentence: ")
    words = sentence.split()
    print(words)

sentence()
   

def multiples_sum():
    n = int(input("Enter a number: "))
    M = 1
    total = 0
    numbers = []    
    for i in range(1, n+1):
        M *= i
        total += i
        numbers.append(str(i))
    print("*".join(numbers), "=", M)
    print("+".join(numbers), "=", total)

multiples_sum()
