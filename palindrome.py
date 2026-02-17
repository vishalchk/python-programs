# =============================
# Palindrome Program 🔄
# =============================

# WAY 1 - Easiest (1 line)
def is_palindrome_easy(word):
    return word == word[::-1]

# WAY 2 - With message
def is_palindrome_string(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# WAY 3 - Using Loop
def is_palindrome_loop(text):
    text = text.lower().replace(" ", "")
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

# Check Number Palindrome
def is_palindrome_number(num):
    original = str(num)
    return original == original[::-1]

# Find all Palindromes in a List
def find_palindromes(words):
    return [word for word in words if is_palindrome_string(word)]

# =============================
# MAIN PROGRAM
# =============================

print("=" * 45)
print("        PALINDROME PROGRAM 🔄")
print("=" * 45)

# String Palindromes
print("\n📝 String Palindrome Check:")
words = ["racecar", "madam", "hello", "level", "python", "civic", "world", "radar"]
for word in words:
    result = "✅ Palindrome!" if is_palindrome_easy(word) else "❌ Not Palindrome!"
    print(f"   {word:10} → reversed: {word[::-1]:10} → {result}")

# Number Palindromes
print("\n🔢 Number Palindrome Check:")
numbers = [121, 123, 1221, 12321, 456, 1001, 999]
for num in numbers:
    result = "✅ Palindrome!" if is_palindrome_number(num) else "❌ Not Palindrome!"
    print(f"   {num:6} → reversed: {str(num)[::-1]:6} → {result}")

# Find all Palindromes
print("\n🔍 Find All Palindromes in List:")
word_list = ["racecar", "apple", "madam", "banana", "level", "python", "civic", "radar"]
palindromes = find_palindromes(word_list)
print(f"   Word List  : {word_list}")
print(f"   Palindromes: {palindromes}")

# Sentence Palindromes
print("\n📖 Sentence Palindrome Check:")
sentences = ["racecar", "Never odd or even", "Hello World", "Was it a car or a cat I saw"]
for sentence in sentences:
    result = "✅ Palindrome!" if is_palindrome_string(sentence) else "❌ Not Palindrome!"
    print(f"   '{sentence}'")
    print(f"    → {result}")

# Palindrome Numbers 1-200
print("\n📊 Palindrome Numbers from 1 to 200:")
palindrome_nums = [n for n in range(1, 201) if is_palindrome_number(n)]
print(f"   {palindrome_nums}")

print("\n" + "=" * 45)
print("       PROGRAM COMPLETE 🎉")
print("=" * 45)
