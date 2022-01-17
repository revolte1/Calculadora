from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc()

@app.get("/")
def read_root():
   return {"Hola": "Mundo"}

@app.get("/sumar")
def call_suma(num1: int = 1, num2: int = 1):
   return {
      "result": calc.sumar(num1, num2)
   }

@app.get("/restar")
def call_suma(num1: int = 0, num2: int = 0):
   return {
      "result": calc.restar(num1, num2)
   }   

@app.get("/multiplicar")
def call_suma(num1: int = 2, num2: int = 5):
   return {
      "result": calc.multiplicar(num1, num2)
   }

@app.get("/dividir")
def call_suma(num1: int = 0, num2: int = 0):
   return {
      "result": calc.dividir(num1, num2)
   }

@app.get("/exponente")
def call_suma(num1: int = 0, num2: int = 0):
   return {
      "result": calc.exponente(num1, num2)
   }