# =============================
# For Loop Examples 🔄
# =============================

print("=" * 40)
print("        FOR LOOP EXAMPLES 🔄")
print("=" * 40)

# 1. Loop through a list
print("\n1️⃣ Loop through a list:")
candies = ["red", "blue", "green", "yellow"]
for candy in candies:
    print(f"   🍬 {candy}")

# 2. Loop through numbers
print("\n2️⃣ Loop through numbers (range):")
for i in range(1, 6):
    print(f"   Number: {i}")

# 3. Loop through a string
print("\n3️⃣ Loop through a string:")
for letter in "Python":
    print(f"   Letter: {letter}")

# 4. Loop with index
print("\n4️⃣ Loop with index (enumerate):")
fruits = ["apple", "banana", "mango"]
for i, fruit in enumerate(fruits):
    print(f"   {i+1}. {fruit}")

# 5. Nested for loop
print("\n5️⃣ Nested for loop (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"   {i} x {j} = {i*j}")

# 6. For loop with break
print("\n6️⃣ For loop with break:")
for i in range(1, 10):
    if i == 5:
        print(f"   Found 5! Stopping! 🛑")
        break
    print(f"   {i}")

# 7. For loop with continue
print("\n7️⃣ For loop with continue (skip even):")
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(f"   {i} (odd)")

# 8. For loop with sum
print("\n8️⃣ For loop with sum:")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"   Numbers: {numbers}")
print(f"   Total  : {total}")

print("\n" + "=" * 40)
print("       PROGRAM COMPLETE 🎉")
print("=" * 40)
