numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

# Solution 1
new_num = []
for number in numbers:
    if type(number) == int:
        new_num.append(number)
print("The result of S1 is", sum(new_num))

# Solution 2
add_num = 0
for number in numbers:
    if type(number) == int:
        add_num += number
print("The result of S2 is", add_num)