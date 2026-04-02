

# 1. Print numbers from 1 to 5
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# 2. Print even numbers from 1 to 10
print("\nEven numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 3. Simple addition using loop
print("\nSum of first 5 numbers:")
total = 0
for i in range(1, 6):
    total += i
print(total)

# 4. Print a simple pattern
print("\nStar Pattern:")
for i in range(1, 6):
    print("*" * i)
