from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates

c = CurrencyRates()

app = Flask(__name__)


@app.route("/")
def show_form():
  """return Forex converter form"""
  
  return render_template("form.html")

@app.route("/submit")
def form_submitted():
  """converts inputs and returns amount"""

  convfrom = request.args.get("convfrom")
  convto = request.args.get("convto")

  return render_template("conversions.html", convfrom=convfrom, convto=convto)
  

