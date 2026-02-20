# =============================
# Prime Number Program 🔢
# =============================


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def list_primes(start, end):
    primes = []
    for value in range(start, end + 1):
        if is_prime(value):
            primes.append(value)
    return primes


# =============================
# MAIN PROGRAM
# =============================

print("=" * 45)
print("       PRIME NUMBER PROGRAM 🔢")
print("=" * 45)

# Check specific numbers
print("\n🧪 Prime check for sample numbers:")
sample_numbers = [2, 3, 4, 5, 9, 11, 17, 21, 29, 35]
for number in sample_numbers:
    result = "✅ Prime" if is_prime(number) else "❌ Not Prime"
    print(f"   {number:3} → {result}")

# Show all primes in a range
print("\n📋 Prime numbers from 1 to 100:")
prime_list = list_primes(1, 100)
print(f"   {prime_list}")

# User input section
print("\n🧠 Check your own number:")
user_input = int(input("   Enter a number: "))
if is_prime(user_input):
    print(f"   ✅ {user_input} is a prime number.")
else:
    print(f"   ❌ {user_input} is not a prime number.")

print("\n" + "=" * 45)
print("       PROGRAM COMPLETE 🎉")
print("=" * 45)
