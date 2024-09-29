import streamlit as st
import random

menu = [
    "Inicio",
    "Saludo simple", 
    "Suma de dos numeros", 
    "Area de un triangulo", 
    "Calculadora de descuento", 
    "Suma de una lista", 
    "Funciones con valores predeterminados", 
    "Numeros pares e impares", 
    "Multiplicacion con *args", 
    "Informacion de una persona con **kwargs", 
    "Calculadora flexible"
]

opciones = st.sidebar.selectbox("Ejercicios", menu)

def ejecutar_programa(opcion):    #funcion mayor para poder ejecutarlo desde el inicio
    match opcion:
        case "Saludo simple":
            st.title("Funcion de saludo simple")
            nombre = st.text_input("Escribe tu nombre:")
            if nombre:
                st.write(f"Hola, {nombre}!")

        case "Suma de dos numeros":
            st.title("Calcular la suma de dos numeros")
            num1 = st.number_input("Ingresa el primer valor:", value=0.0)
            num2 = st.number_input("Ingresa el segundo valor:", value=0.0)
            if st.button("Sumar"):
                resultado = round(num1 + num2, 2)
                st.write(f"La suma de {num1} + {num2} es: {resultado}")

        case "Area de un triangulo":
            st.title("Calcular el area de un triangulo")
            base_str = st.text_input("Ingresa la base:")
            altura_str = st.text_input("Ingresa la altura:")
            if st.button("Calcular"):
                try:
                    base = float(base_str)
                    altura = float(altura_str)
                    resultado = round(base * altura / 2, 2)
                    st.write(f"El area de tu triangulo es: {resultado}")
                except ValueError:
                    st.error("Ingresa valores numericos validos.")

        case "Calculadora de descuento":
            st.title("Calculadora de Precio Final")
            precio_original = st.number_input("Ingresa el precio:", value=0.0)
            cambiar_valores = st.checkbox("Quieres cambiar el descuento y el impuesto?")
            descuento = 10
            impuesto = 16
            if cambiar_valores:
                descuento = st.slider("Selecciona el descuento (10% - 95%):", min_value=10, max_value=95, step=5, value=10)  #no agregue 100% porque no es realista
                impuesto = st.number_input("Ingresa el impuesto:", value=16.0)
            if st.button("Calcular Precio Final"):
                if precio_original > 0:
                    precio_con_descuento = precio_original - (precio_original * descuento / 100)
                    precio_final = precio_con_descuento + (precio_con_descuento * impuesto / 100)
                    st.write(f"El precio final es ${precio_final} con {descuento}% de descuento y {impuesto}% de impuesto")
                else:
                    st.error("Ingresa un valor valido.")

        case "Suma de una lista":
            st.title("Suma de una lista de numeros")
            numeros = st.text_area("Ingresa una lista de numeros separados por comas:")
            if st.button("Sumar"):
                try:
                    lista_numeros = [float(num) for num in numeros.split(",")]
                    resultado = sum(lista_numeros)
                    st.write(f"La suma de los numeros es: {resultado}")
                except ValueError:
                    st.error("Ingresa una lista valida.")

        case "Funciones con valores predeterminados":
            st.title("Funciones con valores predeterminados")
            producto = st.text_input("Ingresa el nombre del producto:")
            cantidad = st.number_input("Cantidad (predeterminado 1):", value=1)
            precio = st.number_input("Precio por unidad (predeterminado 10):", value=10.0)
            if st.button("Calcular Precio Total"):
                precio_total = cantidad * precio
                st.write(f"El total a pagar por {cantidad} {producto}(s) es: ${precio_total}")

        case "Numeros pares e impares":
            st.title("Numeros pares e impares")
            numeros = st.text_area("Ingresa una lista de numeros separados por comas:")
            if st.button("Separar Pares e Impares"):
                try:
                    lista_numeros = [int(num) for num in numeros.split(",")]
                    pares = [num for num in lista_numeros if num % 2 == 0]
                    impares = [num for num in lista_numeros if num % 2 != 0]
                    st.write(f"Numeros pares: {pares}")
                    st.write(f"Numeros impares: {impares}")
                except ValueError:
                    st.error("Ingresa una lista valida.")

        case "Multiplicacion con *args":
            st.title("Multiplicacion con *args")
            numeros = st.text_area("Ingresa una lista de numeros separados por comas:")
            if st.button("Multiplicar todos"):
                try:
                    lista_numeros = [float(num) for num in numeros.split(",")]
                    resultado = 1
                    for num in lista_numeros:
                        resultado *= num
                    st.write(f"El resultado de multiplicar todos los numeros es: {resultado}")
                except ValueError:
                    st.error("Error, ingresa una lista valida.")

        case "Informacion de una persona con **kwargs":
            st.title("Informacion de una persona")
            nombre = st.text_input("Nombre:")
            edad = st.number_input("Edad:", value=0)
            signo = st.text_input("Direccion:")
            profesion =  st.text_input("Profesion:")

            if st.button("Mostrar informacion"):
                if nombre and edad and signo:
                    st.write(f"Te llamas: {nombre}, tienes: {edad} anos, tu signo es: {signo} y eres: {profesion}") #no creo en los signos pero pa poner algo moderno 

                else:
                    st.error("Error, ingresa todos los datos.")

        case "Calculadora flexible":
            st.title("Calculadora flexible")
            num1 = st.number_input("Ingresa el primer numero:", value=0.0)
            num2 = st.number_input("Ingresa el segundo numero:", value=0.0)
            operacion = st.selectbox("Selecciona la operacion:", ["suma", "resta", "multiplicacion", "division"])
            if st.button("Calcular"):
                if operacion == "suma":
                    resultado = num1 + num2
                elif operacion == "resta":
                    resultado = num1 - num2
                elif operacion == "multiplicacion":
                    resultado = num1 * num2
                elif operacion == "division":
                    resultado = num1 / num2 if num2 != 0 else "Error: Division por cero"
                st.write(f"El resultado de la {operacion} es: {resultado}")

if opciones == "Inicio":
    st.title("Bienvenido a nuestra Aplicacion")
    st.write("""
        Aqui encontraras una gran variedad de mini programas realizados con Streamlit. 
        Para comenzar a probarlos, dirigete a la barra lateral izquierda o haz clic en el boton de abajo para abrir uno aleatoriamente.
    """)
    st.write("Esperamos que disfrutes tu experiencia con nuestra aplicacion!")
    st.markdown(
    """
    <style>
        footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 12px;
            color: #555;
        }
    </style>
    <footer>
        <p>© 2024 Mi Aplicacion. Todos los derechos reservados.</p> 
        <p> Desarrollada por Luis Barragan como un proyecto de Programacion Funcional. </p>  
    </footer>
    """,
    unsafe_allow_html=True
)                                                                           #siempre quise poner eso haha

    if st.button("Abrir un programa aleatoriamente"):
        programa_aleatorio = random.choice(menu[1:])
        st.write(f"Se ha abierto el programa: **{programa_aleatorio}**. Disfrutalo!")
        ejecutar_programa(programa_aleatorio)  
else:
    ejecutar_programa(opciones)  
