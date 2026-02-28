# cliclo while 
def suma_digitos(n):
    suma=0
    while n>0:
        el_ultimo_digito= n % 10
        suma += el_ultimo_digito
        n= n //10
    return suma 
print(suma_digitos(5678))


#ciclo for 
def suma_digitos_f(n):
    suma=0
    for i in range(len(str(n))):
        el_ultimo_digito_f= n % 10
        suma += el_ultimo_digito_f
        n= n // 10
    return suma
print(suma_digitos_f(1234))


#recursiva
def suma_digitos_r (n):
    if n==0:
        return 0
    else:
        el_ultimo_digito_r = n%10
        return el_ultimo_digito_r + suma_digitos_r(n//10)
    
print(suma_digitos_r(3456))


