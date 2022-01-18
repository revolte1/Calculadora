from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc()

@app.get("/")
def read_root():
   return {"Hola": "Mundo"}

@app.get("/sumar")
def call_suma(num1: int = 2, num2: int = 0):
   return {
      "result": calc.sumar(num1, num2)
   }

@app.get("/restar")
def call_resta(num1: int = 0, num2: int = 0):
   return {
      "result": calc.restar(num1, num2)
   }   

@app.get("/multiplicar")
def call_multiplicar(num1: int = 0, num2: int = 0):
   return {
      "result": calc.multiplicar(num1, num2)
   }

@app.get("/dividir")
def call_dividir(num1: int = 0, num2: int = 0):
   return {
      "result": calc.dividir(num1, num2)
   }

@app.get("/exponente")
def call_exponente(num1: int = 2, num2: int = 3):
   return {
      "result": calc.exponente(num1, num2)
   }