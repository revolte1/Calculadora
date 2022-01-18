Feature: Exponente dos numeros

    Scenario Outline: Exponente
        Given que quiero realizar operaciones aritméticas
        When acceda <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: exponente de Numeros
        | operacion  | num1 | num2 | result  |
        | exponente  | 2    | 3    | 8       |
        | exponente  | 8    | 2    | 64      |
        | exponente  | 3    | 3    | 27      |
        | exponente  | 0    | 0    | Invalid |
        | exponente  | 2    | -2   | Invalid |