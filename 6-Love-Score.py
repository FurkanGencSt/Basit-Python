name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


true = "true"
love = "love"

result_1 = 0
result_2 = 0
for a in name1.upper():
    for b in true.upper():
        if a == b:
            result_1 += 1
for a in name2.upper():
    for b in true.upper():
        if a == b:
            result_1 += 1

for a in name1.upper():
    for b in love.upper():
        if a == b:
            result_2 += 1
for a in name2.upper():
    for b in love.upper():
        if a == b:
            result_2 += 1

sum = int(str(result_2) + str(result_1))

print(f"Love score {result_1}{result_2}")
if sum < 10 or sum > 90:
    print("Wowowow. You're either going to live together forever or you're about to break up.")
elif sum > 40 and sum < 50:
    print("Cool. Well done ;)")