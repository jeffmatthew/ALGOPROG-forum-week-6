# Review Questions: 
# 1. B
# 2. D
# 3. A
# 4. B
# 5. D
# 6. C
# 7. A
# 8. C
# 9. B

#Programming Exercise:
#1. 
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory)

#2. 
stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}
prices = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}
for food in prices:
    print (food)
    print ("price: %s" % prices[food])
    print ("stock: %s" % stock[food])
total = 0
for fruit in prices:
  gt = prices[fruit] * stock[fruit]
  print(f'The total money earned from {fruit} is {gt}')
  total += gt

#3. 
groceries = ['banana', 'orange', 'apple']
stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}
prices = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total
totalprice = compute_bill(groceries)
print(f'Total: {totalprice}')

#4. 
eren = {
    "name": "Eren",
    "homework": [90.0,97.0,75.0,92.0], 
    "quizzes": [88.0,40.0,94.0],
    "tests": [75.0,90.0]
}
mikasa = {
    "name": "Mikasa",
    "homework": [100.0, 92.0, 98.0, 100.0], 
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
armin = {
    "name": "Armin",
    "homework": [0.0, 87.0, 75.0, 22.0], 
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [eren, mikasa, armin]
for student in students:
    print (student["name"])
    print (student["homework"])
    print (student["quizzes"])
    print (student["tests"])
def average(numbers):
    total = float(sum(numbers))
    average = total/len(numbers)
    return average
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    total = (homework*0.1 + quizzes*0.3 + tests*0.6)
    return total
def get_letter_grade(score):
    if score >= 90: 
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60: 
        return "D"
    else: 
        return "F"
print(f"Mikasa's grade is : {get_letter_grade(get_average(mikasa))}") 
def get_class_average(students):
    results=[]
    for student in students:
        r = get_average(student)
        results.append(r)
    return average(results)
print(f"The class average is : {get_class_average(students)}")
print(f"The class average grade in letter is  : {get_letter_grade(get_class_average(students))} ")