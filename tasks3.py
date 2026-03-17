 # 1. Print numbers from 1 to 50
for i in range(1, 51):
    print(i)

# 2. Even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 3. Odd numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# 4. Multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")

# 5. Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)

# 6. Reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)

# 7. Count numbers divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)

# 8. Squares of 1 to 10
for i in range(1, 11):
    print(i*i)

# 9. Cubes of first 10 numbers
for i in range(1, 11):
    print(i**3)

# 10. Input n, print 1 to n
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i)

    # 11. Print 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1

# 12. Factorial
n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# 13. Reverse a number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)

# 14. Count digits
num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# 15. Keep asking until "stop"
while True:
    text = input("Enter something: ")
    if text.lower() == "stop":
        break

    # 16. *
for i in range(1, 5):
    print("*" * i)

# 17. 1, 12, 123...
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18. Multiplication tables 1–5
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

# 19. A B C pattern
for i in range(3):
    for ch in ['A', 'B', 'C']:
        print(ch, end=" ")
    print()

# 20. 1 to 9 matrix
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

    s = input("Enter string: ")

# 21. Count characters
print(len(s))

# 22. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

# 23. Count consonants
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
print(count)

# 24. Reverse string
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 25. Palindrome check
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

    s = "HelloWorld"

# 26
print(s[:5])

# 27
print(s[-3:])

# 28
print(s[::-1])

# 29
print(s[::2])

# 30
print(s[1:-1])

lst = [10, 20, 30, 40, 50]

# 31. Sum
print(sum(lst))

# 32. Max
print(max(lst))

# 33. Min
print(min(lst))

# 34. Count elements
print(len(lst))

# 35. Check element
x = int(input("Enter element: "))
if x in lst:
    print("Exists")
else:
    print("Not Found")

    lst = [1, 2, 3]

# 36. Append
lst.append(4)
lst.append(5)
lst.append(6)
print(lst)

# 37. Insert at index
lst.insert(1, 100)
print(lst)

# 38. Remove element
lst.remove(100)
print(lst)

# 39. Reverse without reverse()
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print(rev)

# 40. Sort without sort()
lst = [5, 2, 9, 1]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)