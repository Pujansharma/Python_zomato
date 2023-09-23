from flask import Flask, render_template

app = Flask(__name__)
dishes = [
    {"name": "Spaghetti Bolognese", "price": 12.99},
    {"name": "Margherita Pizza", "price": 10.99},
    {"name": "Caesar Salad", "price": 8.99},
    # Add more dishes as needed
]

@app.route('/')
def index():
    return render_template('index.html', dishes=dishes)

if __name__ == '__main__':
    app.run(debug=True)
