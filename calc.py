# チームCの簡単な計算機プログラム


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        raise ValueError("不明な演算子です")


def random_calculation():
    import random

    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(["+", "-", "*", "/", "**", "%"])
    result = calculate(a, b, operator)
    print(f"ランダム計算: {a} {operator} {b} = {result}")


if __name__ == "__main__":
    a = float(input("最初の数値: "))
    operator = input("演算子 (+, -, *, /, **, %): ")
    b = float(input("次の数値: "))

    result = calculate(a, b, operator)
    print(f"{a} {operator} {b} = {result}")

    # ランダム計算を実行
    random_calculation()
