from behave import *
import api
from fastapi.testclient import TestClient

@given('que quiero realizar operaciones aritméticas')
def step_impl(context):
    print("accediendo")
    context.myapp = TestClient(api.app)

@when('acceda {operacion} {num1} y {num2}')
def step_impl(context, operacion, num1, num2):
    context.api_response = context.myapp.get(f"/{operacion}?num1={num1}&num2={num2}")
    assert context.api_response.status_code == 200    


@then('el resultado debe ser {result}')
def step_impl(context, result):
    assert str(context.api_response.json().get("result")) == str(result)