import client

client.receive_file()


def cal(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error! You can't divide by zero!"
        else:
            return num1 / num2
        
def get_num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter the correct number.")


while True:
    op = input("Select (+ - * /) or 'Exit':").lower()
    if op == 'exit':
        break
    
    if op not in ["+", "-", "*", "/", "exit"]:
        print("Unknown operation, please try again!")
        continue
    
    num1 = get_num("Enter the first num: ")
    num2 = get_num("Enter the second num: ")
    
    result = cal(op, num1, num2)
    print(f"Result: {result}")       
    