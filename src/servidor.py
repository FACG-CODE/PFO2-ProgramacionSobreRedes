import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template
import webbrowser
import threading

# Configuración de la base de datos
def inicializar_db():
    conn = sqlite3.connect("persistencia.db")
    try:
        cursor = conn.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                    )
                    ''')
        conn.commit()
        print("Base de datos inicializada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        if conn:
            conn.close()
# Función para registrar un nuevo usuario
def registrar_usuario(username, password):
    conn = sqlite3.connect("persistencia.db")
    try:
        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO usuarios (username, password_hash) 
                    VALUES (?, ?)""", (username, generate_password_hash(password)))
        conn.commit() # Confirmamos los cambios
        return True
    except sqlite3.IntegrityError:
        print("Usuario ya existe.")
        return False
    finally:
        if conn:
            conn.close()
# Función para autenticar un usuario
def autenticar_usuario(username, password):
    conn = sqlite3.connect("persistencia.db")
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM usuarios WHERE username = ?", (username,))
        row = cursor.fetchone() # Captura la fila resultante, o None si no existe
        # Evaluamos si la contraseña hasheada almacenada y la contraseña proporcionada coinciden
        if row and check_password_hash(row[0], password): 
            return True 
        return False 
    except sqlite3.Error as e:
        print(f"Error al autenticar el usuario: {e}")
        return False
    finally:
        if conn:
            conn.close()

# Funcion para integrar flask y renderizar HTML
def iniciar_flask():
    app = Flask(__name__)
    @app.route('/bienvenida')
    def renderizar():
        return render_template('bienvenida.html') # Renderiza el archivo bienvenida.html
    def abrir_navegador():
        webbrowser.open_new("http://127.0.0.1:5000/bienvenida")
    threading.Timer(1, abrir_navegador).start()  # Abre el navegador después de 1 segundo
    app.run(port=5000) # Inicia el servidor Flask en el puerto 5000

# Función para mostrar el menú de consola y manejar la interacción del usuario
def menu_consola():
    while True:
        print("=== Menú de Usuario ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir") # Solo se cierra el programa con esta opción
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            i = 0
            while i < 3:
                usuario = input("Ingrese nombre de usuario: ")
                password = input("Ingrese contraseña: ")
                if usuario.strip() == "" or password.strip() == "":
                    print("El nombre de usuario y la contraseña no pueden estar vacíos.")
                    i += 1
                    continue
                if registrar_usuario(usuario, password):
                    print("Usuario registrado exitosamente.")
                    break
                else:
                    print("Error al registrar el usuario. Intente nuevamente.")
                    i += 1
            else:
                print("Se ha excedido el número máximo de intentos.")
        elif opcion == '2':
            i = 0
            while i < 3:
                usuario = input("Ingrese nombre de usuario: ")
                password = input("Ingrese contraseña: ")
                if usuario.strip() == "" or password.strip() == "":
                    print("El nombre de usuario y la contraseña no pueden estar vacíos.")
                    i += 1
                    continue
                if autenticar_usuario(usuario, password):
                    print("Inicio de sesión exitoso.")
                    iniciar_flask()  # Inicia el servidor Flask y abre el navegador
                else:
                    print("Nombre de usuario o contraseña incorrectos. Intente nuevamente.")
                    i += 1
            else: 
                print("Se ha excedido el número máximo de intentos.")
        elif opcion == '3':
            print("Saliendo del programa.")
            exit(0) 

if __name__ == "__main__": # Corre el programa
    inicializar_db() # Crea la base de datos si no existe
    menu_consola() # Muestra el menú de consola