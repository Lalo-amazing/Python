def palindromos(palabra):
    palabra = palabra.replace(" ","") #replace cambia un caracter por otro, en este caso los espacios por la nada
    palabra = palabra.lower()#lower:todas minusculas, upper: todas mayusculas
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():#run o main para empezar
    palabra=input("Escribe una palabra: ")
    palin = palindromos(palabra)
    if palin == True:
        print("La palabra "+palabra +" Es palindromo")
    else:
        print("La palabra "+palabra +" no es palindromo")


if __name__=="__main__":
    run()
