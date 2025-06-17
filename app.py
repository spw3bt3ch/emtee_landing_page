from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html', titlename = 'Homepage')

@app.route("/order-form")
def order():
  return render_template('order.html', titlename = 'Order form')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5500, debug=True)