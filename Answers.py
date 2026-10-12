# 1
name = input("Enter your name: ")
print(name)

# 2
age = 17
birth_year = 2009
print(age, birth_year)

# 3
a, b = 5, 7
a, b = b, a

# 4
x = [1, 2]
y = x
y.append(3)
print(x)

# 5
a = b = c = 0

# 6
v = 5
v = str(v)
v = list(v)

# 7
big = 1_000_000

# 8
n = None
print(n is None)

# 9
fruits = ["apple", "banana", "cherry", "mango", "kiwi", "pineapple", "orange"]
f1, f2, f3, f4, f5, f6, f7 = fruits

# 10
first, +_, last = (1, 2, 3, 4, 5)
print(first, last)

# 11
MAX_SPEED = 100

# 12
counter = 0
def inc():
    global counter
    counter += 1
inc()

# 13
def make():
    inner = 10
make()

# 14
a = 256; b = 256
print(a is b)
x = 1000; y = 1000
print(x is y)

# 15
p = []
q = p
p.append("item")
print(q)

if (length := len("hello")) > 3:
    print(length)

# 17
num = int(input("Enter a number: "))

# 18
flag = True
print(flag + 5)

# 19
f = 3.9
i = int(f)

# 20
length, width = 5, 3
area = length + width

# 21
full_name = "John Smith"
first_name = full_name[:full_name.index(" ")]

# 22
temp = 10
del temp

# 23
a, b = 2, 3
c = a + b

# 24
original = [1, 2, 3]
copy = original.copy()

# 25
celsius = 30
fahrenheit = celsius * 9/5 + 32

# 26
price = 200
discount_price = price * 0.9

# 27 
s = "100"
n = int(s)

# 28
x, y = 10, 0
z = x / y if y != 0 else None

# 29
sentence = "Python is fun"
sentence_len = len(sentence)

# 30
age = 20
is_adult = age >= 18

# 31
first, last = "Ada", "Lovelace"
full = first + " " + last

# 32
special = "Price: $5 & 10% off! @home #1"
print(special)

# 33
text = """Line one
Line two
Line three"""

# 34
result = 10 > 5  # True

# 35
nums = [4, 5, 6]
first_el = nums[0]

# 36
d = {"name": "Ada", "age": 20}
person_name = d["name"]

# 37
s = {1, 2, 3}
s.add(4)

# 38
t = (1, 2, 3)
# t[0] = 9  # TypeError: tuples are immutable

# 39
v = 3.14
print(type(v))  # <class 'float'>

# 40
c = 3 + 4j

# 41
height_m = 1.75
height_cm = height_m * 100

# 42
seconds = 7265
minutes = seconds / 60
hours = seconds / 3600

# 43
word = "hello"
upper_word = word.upper()

# 44
money = 100
total = money + money * 0.075  # 7.5% tax

# 45
age = "25"
age_in_5 = int(age) + 5

# 46
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3

# 47
pi = 3.14
r = 5
circle_area = pi * r ** 2

# 48
base, exponent = 2, 8
power = base ** exponent

# 49
name = "ADA"
lower_name = name.lower()

# 50
d = {}
d["key"] = "value"

# 51
x = 5
x = x + 1
x = x + 1
x = x + 1
print(x)  # 8

# 52
score = 40
doubled_score = score * 2

# 53
country = "Nigeria"
country_code = "NG"

# 54
binary = "1010"
decimal = int(binary, 2)  # 10

# 55
dec = 10
bin_str = bin(dec)  # '0b1010'
# without prefix: format(dec, "b")

# 56
a, b = 10, 20
avg = (a + b) / 2

# 57
first_name = "Ada"
initial = first_name[0]

# 58
sentence = "I love Python programming"
word_count = len(sentence.split())

# 59
lst = [1, 2, 3]
reversed_lst = lst[::-1]

# 60
d = {"a": 1, "b": 2}
keys_list = list(d.keys())

# 61
print(5 + 3)
# print("5" + 3)  # TypeError: can't add str and int

# 62
age1, age2 = 30, 25
print(age1 - age2)

# 63
print("hi" * 3)  # hihihi

# 64
print(10 / 3)   # 3.333... (true division)
print(10 // 3)  # 3 (floor division)

# 65
print(25 % 4)  # 1

# 66
print(2 ** 10)  # 1024

# 67
x = 10
x += 5

# 68
x = 10
x -= 2   # 8
x *= 3   # 24
x /= 4   # 6.0

# 69
print(25 == 25)

# 70
print(25 != 30)

# 71
print(5 > 3, 5 < 3)

# 72
x = 10
print(5 < x < 15)  # True

# 73
a = [1, 2]
b = [1, 2]
print(a == b)  # True (same value)
print(a is b)  # False (different objects)

# 74
age, has_id = 20, True
print(age > 18 and has_id)

# 75
is_student, is_teacher = True, False
print(is_student or is_teacher)

# 76
raining = False
print(not raining)

# 77
print("a" in "apple")

# 78
d = {"name": "Ada"}
print("name" in d)  # checks keys

# 79
print(10 & 12)  # 8
print(10 | 12)  # 14
print(10 ^ 12)  # 6

# 80
print(8 << 1)  # 16
print(8 >> 1)  # 4

# 81
print(~5)  # -6 (~n == -(n+1))

# 82 precedence: ** first, then *, then +
print(2 + 3 * 4 ** 2)  # 2 + 3*16 = 50

# 83
n = 15
print(n % 3 == 0)

# 84
print(-11 // 3)  # -4 (floors toward negative infinity)

# 85
print(-11 % 3)  # 1 (result takes sign of divisor)

# 86
a, b, c, d, e = 1, 2, 3, 4, 5
print((a + b) * c / d - e)

# 87
print(0 or "hi" and [])  # [] -> "hi" and [] gives [], 0 or [] gives []

# 88
x = None
print(x is None)
print(x is not None)

# 89
print("z" not in "apple")

# 90
r = 4 * 5
print(r % 3)  # 20 % 3 = 2

# 91
x = 17
x //= 5  # 3
x %= 2   # 1

# 92 compound interest
P, r, n, t = 1000, 0.05, 1, 3
amount = P * (1 + r / n) ** (n * t)

# 93
print("apple" < "banana")  # True (alphabetical)

# 94
print([1, 2] + [3, 4])
print([1, 2] * 3)

# 95
print("py" in "python")

# 96
age = 30
print(age >= 18 and age <= 60)

# 97
a, b = 5, 9
print(a if a > b else b)

# 98
weight, height = 70, 1.75
bmi = weight / height ** 2

# 99
total = 135
print(total // 60, total % 60)  # 2 hours 15 minutes

# 100
n = 7
print(n & 1 == 0)  # True if even (lowest bit is 0)

# 101
quantity, price = 3, 9.99
print(quantity * price)

# 102
year = 2010
print(2000 <= year <= 2025)

# 103
user, pw = "ada", "1234"
print(bool(user) and bool(pw))

# 104
print(1234 % 10)  # 4

# 105
print(527 // 100)  # 5

# 106 swap digits of a 2-digit number
n = 47
print((n % 10) * 10 + n // 10)  # 74

# 107
a, b, c = 4, 5, 6
print((a + b + c) / 3)

# 108
a, b, c = 3, 4, 5
print(a + b > c)

# 109
a, b = 5, 9
print((a > b) * a + (a <= b) * b)  # 9

# 110
P, r, t = 1000, 5, 2
si = P * r * t / 100

# 111
a, b = 105, 100
print(abs(a - b) <= 0.10 * b)

# 112
speed, time = 60, 3
distance = speed * time

# 113
c = 100
print(c * 9 / 5 + 32)

# 114
base, height = 10, 5
print(0.5 * base * height)

# 115
cost, sell = 80, 100
print(sell - cost)  # positive = profit, negative = loss

# 116
s = "banana"
print(len(s) > 5 and "a" in s)

# 117
q, r = divmod(17, 5)  # 3, 2

# 118
print(True + False * True)  # 1 + 0 = 1

# 119
print(0 == False, 1 == True)  # True True

# 120
print([] == False)  # False (list is not equal to False)
print(bool([]))     # False (but it is falsy)

# 121
print((10 / 3) * 3)    # 10.0
print((10 // 3) * 3)   # 9

# 122
n = 8
print(n > 0 and n % 2 == 0)

# 123
price = 1500
if price > 1000:
    price *= 0.9

# 124
age = 25
print(not (13 <= age <= 19))

# 125
a, b = "Hello", "World"
c = a + b
print(c, len(a) == len(b))

# 126
a, b = 3, 5
print(a % 2 == 1 and b % 2 == 1)

# 127
price, tax = 200, 7.5
final = price + price * tax / 100

# 128
a, b = 20, 5
print(a % b == 0)

# 129
n = 4
print(n ** 2 - n ** 3)  # -48

# 130
a, b, c, d = True, False, True, True
print((a and b) or (c and d))

# 131
ch = "G"
print("A" <= ch <= "Z")

# 132
n = -5
if n > 0: print("Positive")
elif n < 0: print("Negative")
else: print("Zero")

# 133
age = 19
print("Eligible" if age >= 18 else "Not eligible")

# 134
n = 7
print("Even" if n % 2 == 0 else "Odd")

# 135
y = 2024
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")

# 136
pw = ""
if pw == "":
    print("Password cannot be empty")
elif pw == "secret":
    print("Correct")
else:
    print("Wrong password")

# 137
lst = [1, 2, 3]
if not lst: print("Empty")
else: print(len(lst))

# 138
s = ""
print("Empty" if not s else "Not empty")  # empty string is falsy

# 139
a, b = 5, 9
print(a if a > b else b)

# 140
mark = 65
if mark > 70: print("A")
elif mark > 60: print("B")
elif mark > 50: print("C")
else: print("Fail")

# 141
ch = "7"
if ch.isdigit(): print("Digit")
elif ch.isalpha(): print("Alphabet")
else: print("Special character")

# 142
age = 65
if age >= 18:
    if age > 60: print("Senior citizen")
    else: print("Adult")
else:
    print("Minor")

# 143
light = "yellow"
if light == "red": print("Stop")
elif light == "yellow": print("Get ready")
elif light == "green": print("Go")

# 144
n = 30
print(n % 3 == 0 and n % 5 == 0)

# 145
age = 16
print("Adult" if age >= 18 else "Minor")

# 146
age = 15
print("Child" if age < 13 else "Teen" if age < 20 else "Adult")

# 147
x = 0
print(x is None)   # False
print(x == False)  # True (0 == False)
print(x is False)  # False (0 is not the False object)
x = None
print(x == False, x is None)  # False True

# 148
is_member, price = True, 800
if is_member or price > 1000:
    price *= 0.9
print(price)

# 149
ch = "e"
print("Vowel" if ch.lower() in "aeiou" else "Consonant")

# 150
user, pw = "ada", "1234"
if user == "ada" and pw == "1234": print("Login successful")
else: print("Invalid credentials")

# 151
n = 15
if 1 <= n <= 10: print("1-10")
elif 11 <= n <= 20: print("11-20")
elif 21 <= n <= 30: print("21-30")
else: print("Out of range")

# 152
a, b, c = 3, 4, 5
print(a + b > c and a + c > b and b + c > a)

# 153
a, b, c = 5, 5, 5
if a == b == c: print("Equilateral")
elif a == b or b == c or a == c: print("Isosceles")
else: print("Scalene")

# 154
age, has_license = 20, True
print("Can drive" if age >= 18 and has_license else "Cannot drive")

# 155
n = 456
print(len(str(n)) == 3)

# 156
s = "Python"
print(s[0].isupper())

# 157
lst = [1, 2, 3]
print(2 in lst)

# 158
a, b = "listen", "silent"
print(sorted(a) == sorted(b))

# 159
y = 2000
if y % 100 == 0:
    print("Century, leap" if y % 400 == 0 else "Century, not leap")
else:
    print("Not a century year")

# 160
n = 29
if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# 161
s = "madam"
print(s == s[::-1])

# 162
t = 25
if t < 15: print("Cold")
elif t > 30: print("Hot")
else: print("Normal")

# 163
marks = [45, 60, 70]
print("Pass" if all(m >= 40 for m in marks) else "Fail")

# 164
age, dress = 22, "formal"
print("Entry allowed" if age >= 18 and dress == "formal" else "Denied")

# 165 XOR: one but not both
n = 9
print((n % 2 == 0) != (n % 3 == 0))  # 9: only by 3 -> True

# 166
ch = "#"
if ch.isupper(): print("Uppercase")
elif ch.islower(): print("Lowercase")
elif ch.isdigit(): print("Digit")
else: print("Special")

# 167
hour = 14
if 5 <= hour < 12: print("Morning")
elif 12 <= hour < 17: print("Afternoon")
elif 17 <= hour < 21: print("Evening")
else: print("Night")

# 168
is_student, is_senior, price = False, True, 100
if is_student or is_senior:
    price *= 0.8
print(price)

# 169
pw = "Pass@1234"
strong = (len(pw) > 8
          and any(c.isdigit() for c in pw)
          and any(not c.isalnum() for c in pw))
print("Strong" if strong else "Weak")

# 170
n = 950
print(abs(1000 - n) <= 100 or abs(2000 - n) <= 100)

# 171
email = "ada@mail.com"
print("@" in email and "." in email)

# 172
age = 15
print(13 <= age <= 19)

# 173
x = 3.5
print(isinstance(x, int), isinstance(x, float))

# 174
lst = [1, 2, 2, 3]
print(len(lst) != len(set(lst)))  # True = has duplicates

# 175
print("12345".isdigit())

# 176
print("hello".isalpha())

# 177
f = "photo.jpg"
if f.endswith(".py"): print("Python file")
elif f.endswith(".txt"): print("Text file")
elif f.endswith(".jpg"): print("Image file")
else: print("Unknown")

# 178
import math
n = 49
print(math.isqrt(n) ** 2 == n)

# 179
m = 2
if m == 2: print("28 days")
elif m in (4, 6, 9, 11): print("30 days")
else: print("31 days")

# 180
salary, credit = 150000, 700
print("Eligible" if salary >= 100000 and credit >= 650 else "Not eligible")

# 181
n = 153
digits = str(n)
total = sum(int(d) ** len(digits) for d in digits)
print(total == n)

# 182
a, b = 25, 45
print(a % 10 == b % 10)

# 183
s = "   "
print("Empty or whitespace" if not s.strip() else "Has content")

# 184
age = 70
if age < 12: print("Child ticket")
elif age < 60: print("Adult ticket")
else: print("Senior ticket")

# 185
n = 9
if n > 0:
    if n ** 2 < 100:
        print("Positive and square < 100")

# 186
ans = "Y"
print("Yes" if ans.lower() in ["yes", "y"] else "No")

# 187
lst = [1, 2, 3]
print(lst == sorted(lst))

# 188
d = {}
print("Empty" if not d else "Not empty")

# 189
s = "hello"
print("Even length" if len(s) % 2 == 0 else "Odd length")

# 190
n = 77
print(n % 7 == 0 and n % 10 == 7)

# 191
height, min_height = 140, 120
print("Allowed" if height >= min_height else "Too short")

# 192
s = "Hello"
print(any(c.isupper() for c in s) and any(c.islower() for c in s))

# 193
n = 24
print(n % 4 == 0 and n % 6 == 0)

# 194
grade, attendance = 65, 80
print("Promoted" if grade >= 50 and attendance >= 75 else "Not promoted")

# 195
n = 4
if n == 0: print("Zero")
else:
    if n % 2 == 0: print("Even")
    else: print("Odd")

# 196
m = 7
if m in (12, 1, 2): print("Winter")
elif m in (3, 4, 5): print("Spring")
elif m in (6, 7, 8): print("Summer")
else: print("Autumn")

# 197
u = "adaLove"
print(5 <= len(u) <= 15)

# 198
n = 45
d = len(str(abs(n)))
print("Single" if d == 1 else "Double" if d == 2 else "Triple" if d == 3 else "More")

# 199
s = "Madam"
t = s.lower()
print(t == t[::-1])

# 200
a, b = -3, -7
print((a > 0 and b > 0) or (a < 0 and b < 0))

# 201
print("Hello World".istitle())  # True

# 202
def hello():
    print("Hello World")
hello()

# 203
def greet(name):
    print(f"Hello, {name}!")
greet("Ada")

# 204
def add(a, b):
    return a + b
print(add(2, 3))

# 205
def welcome(name="Guest"):
    print(f"Welcome, {name}")
welcome()
welcome("Ada")

# 206
def rect(l, w):
    return l * w, 2 * (l + w)  # area, perimeter
area, perimeter = rect(5, 3)

# 207
def total(*args):
    return sum(args)
print(total(1, 2, 3, 4))

# 208
def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
show(name="Ada", age=20)

# 209 bug: the default list is created once and shared between calls
def add_item(item, lst=[]):
    lst.append(item)
    return lst
print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] -> surprise!
# fix:
def add_item_fixed(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# 210
count = 0
def increment():
    global count
    count += 1
increment()

# 211
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()
print(outer())

# 212
def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))

# 213
add = lambda a, b: a + b
print(add(2, 3))

# 214 closure
def multiplier(n):
    def times(x):
        return x * n
    return times
double = multiplier(2)
print(double(5))  # 10

# 215
def change(num, lst):
    num += 1        # int is immutable: caller's value unchanged
    lst.append(99)  # list is mutable: caller's list changes
n, l = 1, [1]
change(n, l)
print(n, l)  # 1 [1, 99]

# 216
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 217
def apply(func, value):
    return func(value)
print(apply(str.upper, "hi"))

# 218
def check(n):
    if n < 0:
        return "Negative not allowed"
    return "OK"

# 219 the parameter shadows the global
x = 10
def show_x(x):
    print(x)  # uses the argument, not the global
show_x(5)  # 5
print(x)   # 10

# 220
def length_check(s):
    if (n := len(s)) > 3:
        return f"Long ({n})"
    return f"Short ({n})"

# 221
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

# 222
def is_palindrome(s):
    return s == s[::-1]

# 223
def max3(a, b, c):
    return max(a, b, c)

# 224
def simple_interest(p, t, r=5):
    return p * r * t / 100

# 225
def c_to_f(c):
    return c * 9 / 5 + 32

# 226
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

# 227
def reverse(s):
    return s[::-1]

# 228
def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

# 229
def fact_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 230
def fib_upto(n):
    a, b, out = 0, 1, []
    while a <= n:
        out.append(a)
        a, b = b, a + b
    return out

# 231
def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 232
def is_armstrong(n):
    s = str(n)
    return sum(int(d) ** len(s) for d in s) == n

# 233 power without **
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# 234
def largest(lst):
    big = lst[0]
    for x in lst:
        if x > big:
            big = x
    return big

# 235
def remove_dupes(lst):
    return list(dict.fromkeys(lst))  # keeps order

# 236
def merge(a, b):
    return a + b

# 237
def are_anagrams(a, b):
    return sorted(a.lower()) == sorted(b.lower())

# 238
def count_words(sentence):
    return len(sentence.split())

# 239
def cap_words(s):
    return " ".join(w.capitalize() for w in s.split())

# 240 function inside another
def check_even(n):
    def is_even(x):
        return x % 2 == 0
    return is_even(n)

# 241
def bmi_category(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Normal"
    elif bmi < 30: return "Overweight"
    return "Obese"

# 242
def valid_email(e):
    return "@" in e and "." in e

# 243
def mult_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# 244
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 245
def lcm(a, b):
    return a * b // gcd(a, b)

# 246
def has_digit(s):
    return any(c.isdigit() for c in s)

# 247
def sum_even(*args):
    return sum(x for x in args if x % 2 == 0)
print(sum_even(1, 2, 3, 4))  # 6

# 248
def greeting(name):
    return "Good day, " + name + "! Welcome."

# 249
def second_largest(lst):
    unique = sorted(set(lst))
    return unique[-2] if len(unique) >= 2 else None

# 250
def strong_password(pw):
    return (len(pw) >= 8
            and any(c.isdigit() for c in pw)
            and any(c.isupper() for c in pw)
            and any(not c.isalnum() for c in pw))

# 251
def to_hm(minutes):
    return str(minutes // 60) + "h " + str(minutes % 60) + "m"

# 252
def discount(price):
    return price * 0.9 if price > 1000 else price

# 253
def vote_message(age):
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"

# 254
def full_name(first, last):
    return first + " " + last

# 255
def circle_area(r, pi=3.14159):
    return pi * r ** 2

# 256
def info():
    return "Ada", 20, "Lagos"
name, age, city = info()

# 257
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# 258
import math
def is_perfect_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n

# 259
def pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

# 260
def average(lst):
    return sum(lst) / len(lst) if lst else 0

# 261
def is_sorted(lst):
    return lst == sorted(lst)

# 262
first, last = "Ada", "Lovelace"
print(first + " " + last)

# 263
name, age = "Ada", 20
print(name + " is " + str(age))  # age must be converted with str()

# 264
print("word " * 10)

# 265
name, age = "Ada", 20
print(f"{name} is {age}")

# 266
print("{} is {}".format(name, age))

# 267
words = ["I", "love", "Python"]
print(" ".join(words))

# 268
n = 5
print(f"Number: {n}")        # f-string handles the conversion
print("Number: " + str(n))   # + needs str()

# 269
print("Hello" + "")  # Hello

# 270
val = None
# print("Value: " + val)  # TypeError: can't concat str and None
print("Value: " + str(val))    # fix: Value: None
print("Value: " + (val or ""))  # or treat None as empty

# 271
nums = [1, 2, 3]
print(",".join(map(str, nums)))  # 1,2,3

# 272
flag = True
print("Flag: " + str(flag))
print(f"Flag: {flag}")

# 273
print(f"{2+3}=5")  # 5=5

# 274
s = "Hello"
print(s + s[::-1])  # HelloolleH

# 275 implicit concat (literals only)
print("hello" "world")  # helloworld

# 276
print("Hello".__add__(" World"))

# 277
words = ["I", "love", "Python"]
print(" ".join(words))       # join: fast and clean
result = ""
for w in words:
    result += w + " "        # loop with +: slower for big lists
print(result.strip())

# 278
a = "Line one\n" + "Line two"
b = """Line one
Line two"""

# 279
import os
print(os.path.join("home", "user", "docs"))  # joins with the OS separator
print("/".join(["home", "user", "docs"]))    # home/user/docs

# 280
name, domain = "ada", "mail.com"
print(name + "@" + domain)

# 281
price = 5.5
print(f"Price: {price:.2f}")  # Price: 5.50

# 282
first, last = "Ada", "Lovelace"
print(first[0] + last[0])  # AL

# 283
nums = [1, 2, 3]
print(["Item " + str(n) for n in nums])

# 284
combined = "Hello" + "World"
print("World" in combined)

# 285
print("Wow" + "!!!" * 3)  # Wow!!!!!!

# 286
print("-".join(["a", "b", "c"]))  # a-b-c

# 287
print("Line1" + "\n" + "Line2")

# 288
print(("hello" + " world").upper())

# 289
c = "Hello" + "World"
print(len(c))

# 290
s = "Hi"
print(f"{s}{s}")  # HiHi

# 291
name = input("Name: ")
print("Hello, " + name + "!")

# 292
city, country = "Lagos", "Nigeria"
print(city + ", " + country)

# 293
s = "Hello" + " World"
print(s.replace("World", "Python"))

# 294
s = "abc" + "def" + "ghi"
print(s[2:6])  # cdef

# 295
s = "5" + "3"   # "53"
print(int(s) * 2)  # 106

# 296
items = ["a", "b", "c"]
print(",".join(items))
print("-".join(items))
print("|".join(items))

# 297
a, b = True, False
print(str(a) + str(b))  # TrueFalse

# 298
print("Name" + "\t" + "Age")

# 299 three methods
name, age = "Ada", 20
print("I am " + name + " and I am " + str(age) + " years old")  # 1: +
print(f"I am {name} and I am {age} years old")                  # 2: f-string
print("I am {} and I am {} years old".format(name, age))        # 3: format()

# 300
a, b = "ab", "ba"
c = a + b
print(c == c[::-1])  # abba -> True
