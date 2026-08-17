# teamC

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "**":
        return a ** b
    elif operator == "%":
        return a % b
    elif operator == "//":
        return a // b
    elif operator == "sqrt":
        if a < 0:
            raise ValueError("負の数の平方根は計算できません")
        return a ** 0.5
    else:
        raise ValueError("不明な演算子です")

if __name__ == "__main__":
    a = float(input("最初の数値: "))
    operator = input("演算子 (+, -, *, /, **, %, //, sqrt): ")
    b = float(input("次の数値: "))

    result = calculate(a, b, operator)
    print(f"{a} {operator} {b} = {result}")