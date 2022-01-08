Feature: multiplicar dos numeros

    Scenario Outline: multiplicar
        Given que quiero realizar operaciones aritméticas
        When acceda <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: multiplicar de Numeros
        | operacion      | num1 | num2 | result  |
        | multiplicar    | 2    | 1    | 2       |
        | multiplicar    | 8    | 8    | 64      |
        | multiplicar    | 3    | 100  | 300     |
        | multiplicar    | 0    | 0    | 0       |
        | multiplicar    | 1    | -2   | Invalid |