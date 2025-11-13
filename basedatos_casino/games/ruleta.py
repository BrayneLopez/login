import random

#CASINO CON LOGIN Y 2 JUEGOS EN UN MENU PRINCIPAL, CON CONFIG DE CAMBAIR NOMBRE, ANADIR UN APODO O ELIMINAR CUENTA.
#EN LA BD 2 USUARIOS TENDRAN 20K DE SALDO EL CUAL USARAN EN AMBOS JUEGOS, PODRA RETIRAR Y DEPOSITAR.
#CON UN IMPORT FUNCION ; PODRAN RECIBIR EL DINERO EN OTRA CARPETA QUE SIMULE UNA APP DE AHORROS DONDE TENDRAN REGISTRO DE TRANSACCION.
#JUEGO 1; BLACKJACK21 - JUEGO 2; RULETA RED-BLACK + NUMERO PAR E IMPAR

base_datos = {
    
    "id:588":{'nombre':'brayner',
    'correo':'brainer98@gmail.com',
    'saldo':2000,
    'contrasena':'12345l'},
    
    "id:589":{'nombre':'juan',
    'correo':'juanlim@gmail.com',
    'saldo':6000,
    'contrasena':'123lop'
    }
}

color = None
result = 0
user_option_apuesta = 0


def ruleta_colores(): #funcion
    colores_secuencia = ["Verde", "Rojo", "Negro"]
    p = random.choice(colores_secuencia)
    return p


secu = ruleta_colores()
            
            
def desicion_juego(p):
    verde = 0
    rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negro = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        
    if p.lower() == "verde":
        return verde, p
    elif p.lower() == "rojo":
        r = random.choice(rojo)
        return r, p
    elif p.lower() == "negro":
        n = random.choice(negro)
        return n, p
    
    
result, color, = desicion_juego(secu)

            
def dinero_apuesta():
    global user_option_apuesta
    try:
        user_option_apuesta = int(input("Cantidad Apuesta:"))
        while base_datos.get('saldo') < 1000 or user_option_apuesta < 1000:
            print("La Cantidad del saldo es Insuficienten" )
            menu_principal()
        menu_ruleta_casino()
    except ValueError:
        print("No puedes usar letras en este campo.\n")
        user_option_apuesta = int(input("Cantidad Apuesta:"))
        
    return user_option_apuesta
        
        
def menu_ruleta_casino():
    global user_option_apuesta
    print("""Menu>   
    1.Color Rojo
    2.Color Negro
    3.Numero Par
    4.Numero Impar
    5.Numero Seleccionado\n
    """)
    user_option = input("Opcion de Juego:\n")
    if user_option in ["uno", "1", "rojo", "red", "color r"]:
        print(f"Resultado :{color} {result}")
        if "Rojo" == color:
            s = user_option_apuesta * 1
            base_datos['saldo'] += s           
            dinero_apuesta()
            menu_ruleta_casino()
            return s
        else:
            base_datos['saldo'] -= user_option_apuesta
            
            dinero_apuesta()
            menu_ruleta_casino()
    elif user_option in ["2", "dos", "two", "color n", "negro"]:
        print(f"Resultado :{color} {result}")
        if color.lower() in ["2", "dos", "two", "color n", "negro"]:
            s = user_option_apuesta * 1
            base_datos['saldo'] += s
            ruleta_colores
            menu_ruleta_casino()
            return s
        else:
            base_datos['saldo'] -= user_option_apuesta
            dinero_apuesta()
            menu_ruleta_casino()
            
    elif user_option in ["3", "tres", "par", "numero p"]:
        if result % 2 == 0:
            print(f"Resultado :{color} {result} PAR")
            s = user_option_apuesta * 1
            base_datos['saldo'] += s
            dinero_apuesta()
            menu_ruleta_casino()
            return s
        
        else:
            print("IMPAR")
            base_datos['saldo'] -= user_option_apuesta
            dinero_apuesta()
            menu_ruleta_casino()
            
    elif user_option in ["4", "cuatro", "impar", "numero i"]:
        if result % 2 == 0:
            print(f"Resultado :{color} {result} IMPAR")
            s = user_option_apuesta * 1
            base_datos['saldo'] += s
            dinero_apuesta()
            menu_ruleta_casino()
            return s
        
        else:
            print("PAR")
            base_datos['saldo'] -= user_option_apuesta
            dinero_apuesta()
            menu_ruleta_casino()
            
    elif user_option in ["5", "cinco", "numero s", "five"]:
        num_x = int(input("Numero:"))
        print(f"Resultado :{color} {result}")
        
        if num_x == result:
            s = user_option_apuesta * 1
            base_datos['saldo'] += s
            dinero_apuesta()
            menu_ruleta_casino()
            
        else:
            base_datos['saldo'] -= user_option_apuesta
            dinero_apuesta()
            menu_ruleta_casino()
        
        
def menu_principal():
    print("""MENU>
    1. RuletaRed+Black
    2. BlackJack21
    3. Cuenta
    4. Salir de Sesion""")
    optiones = input("Eleccion:")
    
    if optiones in ["1", "uno", "black", "one"]:
        dinero_apuesta()

if __name__ == '__main__':
    
    menu_principal()


 


        
        
    


            