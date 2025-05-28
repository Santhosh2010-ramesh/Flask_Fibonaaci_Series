from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]

@app.route('/')
def home():
    return "Welcome to Fibonacci Service!"

@app.route('/fibonacci')
def get_fibonacci():
    n = int(request.args.get('n', 10))
    return jsonify(fibonacci(n))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
