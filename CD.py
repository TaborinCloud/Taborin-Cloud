import os
import sys
import time
import pyfiglet

# Función para limpiar la consola antes de imprimir la salida
def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cifrar_texto(texto):
    abecedario = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
        'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
        'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    texto_cifrado = []
    for caracter in texto:
        if caracter.isalpha():
            texto_cifrado.append(str(abecedario[caracter.upper()]))
        elif caracter == ' ':
            texto_cifrado.append('/')  # marcador de separación entre palabras
        else:
            texto_cifrado.append(caracter)
    return ' '.join(texto_cifrado)

def descifrar_texto(cifrado):
    abecedario_invertido = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
        8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
        15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
        22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    }
    elementos = cifrado.split()
    texto_descifrado = []
    for elemento in elementos:
        if elemento.isdigit():
            texto_descifrado.append(abecedario_invertido[int(elemento)])
        elif elemento == '/':
            texto_descifrado.append(' ')
        else:
            texto_descifrado.append(elemento)
    return ''.join(texto_descifrado)

def firma():
    print("Create by JCode 2025© ||")
    print("De: Cavallo Joquin    ||")
    print("-----------------------")

def main():
    print()
    print("Bienvenido al Sistema de Codificacion y Decodificacion.")
    print()

def mostrar_logo():
    logo = pyfiglet.figlet_format("JCode")
    print(logo)

password = "tbc" ###############

def login():

    acceso_concedido = False

    while not acceso_concedido:
        usuario = inputt("Usuario: ").strip()
        if not usuario:
            print("\033[91mEl nombre de usuario no puede estar vacío.\033[0m")
            continue

        codigo = input("Código de Acceso: ").strip()
        if not codigo:
            print("\033[91mEl campo de contraseña no puede estar vacío.\033[0m")
            continue

        if codigo != password:
            print("\033[91mContraseña incorrecta. Intenta de nuevo.\033[0m")
            continue
        acceso_concedido = True

        while True:
            main()
            opcion = input("¿Deseas cifrar, descifrar o salir? (cifrar/descifrar/ayuda/salir): ").strip().lower()
            if opcion == "ayuda":
                print('Proximamente')
                break
                      
            if opcion == "salir":
                print("Gracias por usar el sistema.")
                break
            elif opcion in ("cifrar", "descifrar"):
                texto = input("Introducir Texto-->: ").strip()
                limpiar_consola()
                firma()
                if opcion == "cifrar":
                    texto_cifrado = cifrar_texto(texto)
                    barra_carga()
                    print()
                    print("Texto Cifrado:", texto_cifrado)
                elif opcion == "descifrar":
                    texto_descifrado = descifrar_texto(texto)
                    barra_carga()
                    print()
                    print("Texto Descifrado:", texto_descifrado)
            else:
                print("\033[91mOpción no válida. Elige 'cifrar', 'descifrar' o 'salir'\033[0m")

def barra_carga(total=30):
    for i in range(total + 1):
        porcentaje = int((i / total) * 100)
        barra = '=' * i + ' ' * (total - i)
        sys.stdout.write(f'\r\033[92m[{barra}]\033[0m {porcentaje}%')
        sys.stdout.flush()
        time.sleep(0.1)
        
def barra_carga_inicio(total=30):
    for i in range(total + 1):
        porcentaje = int((i / total) * 100)
        barra = '=' * i + ' ' * (total - i)
        sys.stdout.write(f'\r\033[92m[{barra}]\033[0m {porcentaje}% --> Loading...')
        sys.stdout.flush()
        time.sleep(0.2)

# Ejecutar el sistema
if __name__ == "__main__":
    barra_carga_inicio()
    barra_carga()
    limpiar_consola()
    print()
    mostrar_logo()
    firma()
    login()
    
    
 
#print("\033[91mTexto en rojo\033[0m")
#print("\033[92mTexto en verde\033[0m")
#print("\033[93mTexto en amarillo\033[0m")
#print("\033[94mTexto en azul\033[0m")
