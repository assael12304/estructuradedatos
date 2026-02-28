# WHile
def es_palindromo_w(texto):
    # preprocesamiento
    texto_limpio = ""
    i = 0
    while i < len(texto):
        if texto[i] != " ":
            texto_limpio += texto[i].lower()
        i += 1

    # comparacion con while
    izq = 0
    der = len(texto_limpio) - 1
    while izq < der:
        if texto_limpio[izq] != texto_limpio[der]:
            return False
        izq += 1
        der -= 1
    return True

print(es_palindromo_w("anita"))       # True
print(es_palindromo_w("racecar"))     # True
print(es_palindromo_w("python"))      # False


# for 
def es_palindromo_f(texto):
    # preprocesamiento
    texto_limpio = ""
    for char in texto:
        if char != " ":
            texto_limpio += char.lower()

    # comparacion con for
    for i in range(len(texto_limpio) // 2):
        if texto_limpio[i] != texto_limpio[-(i + 1)]:
            return False
    return True

print(es_palindromo_f("anita"))       # True
print(es_palindromo_f("racecar"))     # True
print(es_palindromo_f("python"))      # False


# RECURSIVA
def es_palindromo_r(texto):
    # preprocesamiento solo al inicio
    texto = texto.replace(" ", "").lower()

    # caso base
    if len(texto) <= 1:
        return True
    # si los extremos difieren
    if texto[0] != texto[-1]:
        return False
    # caso recursivo
    return es_palindromo_r(texto[1:-1])

print(es_palindromo_r("anita"))            # True
print(es_palindromo_r("racecar"))          # True
print(es_palindromo_r("python"))           # False
print(es_palindromo_r("A man a plan"))     # True

