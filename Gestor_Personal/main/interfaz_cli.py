import subprocess 
import os
from decimal import Decimal
from datetime import datetime



# Funciones de salida de consola

## Selección

def ver_titulo():
    titulo = ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       Bienvenido a tu gestor personal
           (cortesía de Stapaher)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    limpiar_consola()
    print(titulo)

def ver_menu_opcion():
    menu_opcion = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                O p c i o n e s
----------------------------------------------
      1. Gestiones          2. Reportes     
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
------------------ 0. Salir ------------------
"""
    limpiar_consola()
    ver_titulo()
    print(menu_opcion)

def ver_menu_gestion():
    menu_gestion = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              G e s t i o n e s              
----------------------------------------------
   1. Añadir     2. Modificar  3. Borrar    
----------------------------------------------
   1. Entrada    2. Salida     3. Recurrencia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
----------------- 0. Inicio ------------------ 

Para seleccionar introduce, Ej: 1.1

    """
    limpiar_consola()
    ver_titulo()
    print(menu_gestion)

def ver_menu_reporte():
    menu_reporte = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               R e p o r t e s
----------------------------------------------
   1. Total     2. Mensual    3. Estadístico 
----------------------------------------------
   1. Entrada   2. Salida     3. Recurrencia 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
----------------- 0. inicio ------------------

Para seleccionar introduce, Ej: 1.1

    """
    limpiar_consola()
    ver_titulo()
    print(menu_reporte)


def ver_mensaje_salida():
    mensaje_salida = """\n
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!Que tengas un buen día, hasta luego.¡
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 
    """
    print(mensaje_salida)


## Información de movimientos

def ver_formulario_entrada(concepto, 
                           importe, 
                           fecha_efectiva, 
                           recurrencia, 
                           nota
):
    
    formulario_entrada = f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    M O V I M I E N T O  —  E N T R A D A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Movimiento preparado: {recurrencia}
---------------------------------------------
Concepto:         {concepto}
Importe:          {importe}
Fecha efectiva:   {fecha_efectiva}
---------------------------------------------
Nota : {nota}
---------------------------------------------
"""
    print(formulario_entrada)

def ver_formulario_salida(concepto, 
                           importe, 
                           fecha_efectiva, 
                           recurrencia, 
                           nota
):
    formulario_salida = f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     M O V I M I E N T O  —  S A L I D A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Movimiento preparado: {recurrencia}
---------------------------------------------
Concepto:         {concepto}
Importe:          {importe}
Fecha efectiva:   {fecha_efectiva}
---------------------------------------------
Nota : {nota}
---------------------------------------------
"""
    print(formulario_salida)

def ver_formulario_modificacion(motivo_modificacion, 
                                tipo, 
                                concepto, 
                                importe, 
                                fecha_efectiva, 
                                recurrencia,
                                nota,
):
    formulario_modificacion = f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           M O D I F I C A C I Ó N
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Motivo modificación: {motivo_modificacion}
---------------------------------------------
Movimiento preparado: {recurrencia}
---------------------------------------------
Tipo:             {tipo}
Concepto:         {concepto}
Importe:          {importe}
Fecha efectiva:   {fecha_efectiva}
---------------------------------------------
Nota : {nota}
---------------------------------------------
"""
    print(formulario_modificacion)

def ver_movimiento(tipo, 
                   identificador, 
                   concepto, 
                   importe, 
                   fecha_efectiva, 
                   nota, 
                   recurrencia
):
    movimiento = f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                {tipo}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ID: {identificador}

Concepto: {concepto}
Importe: {importe}
Fecha efectiva: {fecha_efectiva}
---------------------------------------------
Nota: {nota}
---------------------------------------------
Movimiento recurrente: {recurrencia}
---------------------------------------------
    """
    print(movimiento)



## Funciones de solicitud (La responsabilidad de éstas funciones es: "DEVOLVER UNA OPCIÓN VÁLIDA A MAIN")

def solicitar_opcion():
    opciones_validas = (0, 1, 2)
    opcion_introducida = input("¿Qué necesitas hacer?:  ")
    try:
        opcion = int(opcion_introducida)
        if opcion in opciones_validas:
            return opcion
        else:
            print(f"\n ERROR : >>> OPCIÓN: ==> {opcion_introducida} <== | INOPERABLE | <<<\n\n            >>> PRUEBA OTRA VEZ <<<\n")
            esperar_continuar()
            limpiar_consola()
            return None
    except ValueError as error:
        error = (f"\n ERROR : >>> OPCIÓN: ==> {opcion_introducida} <== | INVÁLIDA | <<<\n\n           >>> PRUEBA OTRA VEZ <<<\n")
        print(error)
        esperar_continuar()
        return None

def solicitar_gestion():
    opciones_validas = ("0",
        "1.1", "1.2", "1.3",
        "2.1", "2.2", "2.3",
        "3.1", "3.2", "3.3")
    opcion_gestion = (input("¿Qué operación deseas ejecutar?: "))
    if opcion_gestion in opciones_validas:
        return opcion_gestion
    else:
        print("\n ERROR : >>> OPCIÓN DE GESTIÓN | INVÁLIDA | <<<\n")
        esperar_continuar()
        limpiar_consola()
        return None

def solicitar_reporte():
    opciones_validas = ("0",
        "1.1", "1.2", "1.3",
        "2.1", "2.2", "2.3",
        "3.1", "3.2", "3.3")
    opcion_reporte = (input("¿Qué necesitas consultar?: "))
    if opcion_reporte in opciones_validas:
        return solicitar_reporte()
    else:
        print("\n ERROR : >>> OPCIÓN DE REPORTE | INVÁLIDA | <<<\n")
        limpiar_consola()
        return solicitar_reporte

def solicitar_confirmacion():
    confirmacion = input("        ¿Confirmar movimiento?   [S/N]: ").upper()
    if confirmacion == "S" or confirmacion == "SI":
        return True
    elif confirmacion == "N" or confirmacion == "NO":
        return False
    else:
        print("\n ERROR : >>> TIPO DE CONFIRMACIÓN | INVÁLIDA | <<<\n")
        limpiar_consola()
        return solicitar_confirmacion()



### Introducción de información persistente

def solicitar_concepto():
    concepto = input("\nIntroduce el concepto: ")
    if len(concepto) <= 1 or len(concepto) > 100:
        print("\n ERROR : >>> CONCEPTO FUERA DE RANGO <<<")
        return solicitar_concepto()
    return concepto

def solicitar_importe():
    try:
        importe = Decimal(input("\nIntroduce el importe: ")).quantize(Decimal("0.0000"))
        return importe
    except ValueError:
        raise ValueError(" ERROR : >>> FORMATO IMPORTE <<<")

def solicitar_fecha_efectiva():                                                                             # SI AL INTRODUCIR CUALQUIER CADENA DE CARACTERES QUE NO SEA UNA FECHA, EJ ASDFDF, NO DEVUELVE ERROR - PENDIENTE DE SOLUCIONAR.
    
    fecha_efectiva = datetime
    fecha_introducida = input("\nIntroduce la fecha efectiva del movimiento (dd/mm/aa): ")

    if fecha_introducida.isdigit():
        try:
            if len(fecha_introducida) == 8:
                dia = fecha_introducida[0:2]
                mes = fecha_introducida[2:4]
                anio = fecha_introducida[4:8]

                fecha_efectiva = f"{dia}/{mes}/{anio}"
                                
                return fecha_efectiva
            
            elif len(fecha_introducida) == 6:
                dia = fecha_introducida[0:2]
                mes = fecha_introducida[2:4]
                anio = "20" + fecha_introducida[4:6]
            
                fecha_efectiva = f"{dia}/{mes}/{anio}"
                
                return fecha_efectiva
        
        except Exception:
            print(" ERROR : >>> FORMATO FECHA EFECTIVA <<<\n FECHA RECIBIDA : ", fecha_introducida, "\n")
            esperar_continuar()
            limpiar_consola()
            return solicitar_fecha_efectiva()

    elif not fecha_introducida.isdigit():
        try:
            fecha_introducida = fecha_introducida.replace("-", "/")
            fecha_introducida = fecha_introducida.replace(".", "/")   
            fecha_introducida = fecha_introducida.replace(" ", "/")               

            return fecha_introducida
        
        except ValueError:
            print(" ERROR : >>> FORMATO FECHA EFECTIVA <<<\n FECHA RECIBIDA : ", fecha_introducida, "\n")
            esperar_continuar()
            limpiar_consola()
            return solicitar_fecha_efectiva()
    else:
        print(f" ERROR : >>> NO ENTIENDO LA FECHA RECIBIDA: {fecha_introducida} <<<\n")
        esperar_continuar()
        limpiar_consola()
        return solicitar_fecha_efectiva()

    normalizar_fecha_efectiva(fecha_efectiva)

def solicitar_recurrencia():
    pass

def solicitar_nota():
    nota = input("\n¿Quieres añadir información adicional?: ")
    return nota

def solicitar_motivo_modificación():
    motivo = input("Introduce la causa de la modificación: ")
    motivo.strip
    if len(motivo) <= 1 or len(motivo) > 100:
            print("\n ERROR : >>> MOTIVACIÓN FUERA DE RANGO <<<")
            return solicitar_motivo_modificación()
    return motivo



### Limpieza consola (Ésta función evita que se extienda la consola)

def esperar_continuar():
    input("\nPresiona > Enter < para continuar...\n")

def limpiar_consola():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def normalizar_fecha_efectiva(fecha_introducida):
    
    try:
        fecha_normalizada = datetime.strptime(fecha_introducida, "%d/%m/%y").date()
        return fecha_normalizada
    
    except TypeError, Exception:
        print("\n  ERROR : >>> NORMALIZACIÓN FECHA INTRODUCIDA <<<")
        esperar_continuar()
        limpiar_consola()
        return solicitar_fecha_efectiva()



