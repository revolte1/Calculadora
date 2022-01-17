Feature: Exponente dos numeros

    Scenario Outline: Exponente
        Given que quiero realizar operaciones aritméticas
        When acceda <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: exponente de Numeros
        | operacion  | num1 | num2 | result  |
        | exponente    | 2    | 1    | 2.0     |
        | exponente    | 8    | 2    | 64.0    |
        | exponente    | 3    | 3    | 27.0    |
        | exponente    | 0    | 0    | Invalid |   
        | exponente    | 2    | -2   | Invalid |