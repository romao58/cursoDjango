# import numpy as np
from ClassePython import Calculadora


var_a = 2
var_b = 3
calc = Calculadora(5,8)

print(calc.soma())

var_r = var_a + var_b

if var_r == 5:
    print("Passou")
else:
    print("Falhou")
