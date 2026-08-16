import math

#consultamos al usuario los numeros y la operacion a realizar

num1=input("numero 1: ")
num2=input("numero 2:  ")
pregunta=input("operacion (+,-,*,/,funcion):")

#realizamos la operacion segun lo que el usuario haya ingresado

if pregunta== "+":
      resultado=float(num1)+ float(num2)
      print(f"el resultado es: {resultado}")
elif pregunta== "-":
     resultado=float(num1)-float(num2)
     print(f"el resultado es: {resultado}")
elif pregunta== "*":
      resultado=float(num1)*float(num2)
      print(f"el resultado es: {resultado}")
elif pregunta== "/":
     resultado=float(num1)/float(num2)
     print(f"el resultado es: {resultado}")
elif pregunta !="+" and pregunta !="-" and pregunta !="*" and pregunta !="/" and pregunta !="funcion":
    print("operacion invalida")
    
elif pregunta== "funcion":
    function=input("ingrese la funcion (sqrt,log,sen,cos,tan): ")
    if function=="sqrt":
        resultado=math.sqrt(float(num1))
        print(f"el resultado es: {resultado}")
    elif function=="log":
        resultado=math.log(float(num1))
        print(f"el resultado es: {resultado}")
    elif function=="sen":
        resultado=math.sin(float(num1))
        print(f"el resultado es: {resultado}")
    elif function=="cos":
        resultado=math.cos(float(num1))
        print(f"el resultado es: {resultado}")
    elif function=="tan":
        resultado=math.tan(float(num1))
        print(f"el resultado es: {resultado}")
else: print("funcion invalida")
    
    
     
    
