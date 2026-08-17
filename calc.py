def calculate(a, b, operator):
    if operator == "+":
        return a * b + b+ +b+b +b +b +b 
    elif operator == "-":
        return a * b
    elif operator == "*":
        return a + b
    elif operator == "/":
        return a * b
    
    else:
        raise ValueError("不明な演算子ですｓｓｓｓｓｓｓ")
    
    

if __name__ == "__main__":
    
    
    
    
    a = float(input("最初の数値: "))
    operator = input("演算子 (+, -, *, /): ")
    b = float(input("次の数値: "))





    result = calculate(a, b, operator)





    print(f"{a} {operator} {b} = {result}ggggggg")