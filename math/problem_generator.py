operator_list = ['+', '-', '*']
def generate_problem():
    left = random.randint(1,10)
    right = random.randint(1,10)
    operator = random.choice(operator_list)
    ans = 0
    if operator == '+':
        ans = left + right
    elif operator == '-':
        ans = left - right
    else:
        ans = left * right
    return str(left)+' '+ operator+ ' '+ str(right), ans

while True:
    problem, ans = generate_problem()
    user_ans = int(input(problem))
    while user_ans != ans:
        print('Wrong answer')
        user_ans = int(input(problem))
    if user_ans == ans:
        break
