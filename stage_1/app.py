from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
""" checks if a number is a prime """
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


def digit_sum(n):
    return sum(int(d) for d in str(n))

"""
An Armstrong number (Narcissistic number) is a number
that is equal to the sum of its digits raised
to the power of the number of digits.
"""
def is_armstrong(n):
    """
    check is a number is armstrong.
    """
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_perfect(n):
    """ checks if  number is perfect """
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

@app.route("/api/classify-number", methods=["GET"])
def classify_numbers():
    num = request.args.get("number")
    if not num or not num.lstrip('-').isdigit():
        return jsonify({"number": num, "error": True}), 400
    num = int(num)
    url = f'http://numbersapi.com/{num}'
    res = requests.get(url)
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("even" if num % 2 == 0 else "odd")
    return jsonify({
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum(num),
        "fun_fact": res.text if res.text else None
        })



if __name__=="__main__":
    app.run()
