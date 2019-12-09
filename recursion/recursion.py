
def recursion(input):
    if input < 25:
        print(f"Input data is: {input}")
        input += 1
        # проводимо стан через рекурсивний виклик
        recursion(input)

    else:
        # повертаємо фінальний результат
        print(f"Algorith ends at {input}")

    #return input

# https://realpython.com/python-thinking-recursively/
def factorial_recursive(input):
    # базовий випадок 1! = 1
    if input == 1:
        return 1
    # рекурсивний випадок n! = n * (n-1)!
    else:
        return input * factorial_recursive(input - 1)

# сума 1+2+3+4+...+9+10
def recursion_sum(current_number, acumulated_sum):
    if current_number == 11:
        return acumulated_sum
    else:
        return recursion_sum(current_number + 1, acumulated_sum + current_number)


if __name__ == "__main__":
    recursion(1)
    #print("",factorial_recursive(10))
    #print("", recursion_sum(1, 0))