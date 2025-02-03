from flask import Flask, request, jsonify
import requests
from is_prime import is_prime 
from is_perfect import is_perfect
from is_armstrong import is_armstrong
from digit_sum import digit_sum

app = Flask(__name__)

@app.route("/numbers/classify-number", methods=["GET"])
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
