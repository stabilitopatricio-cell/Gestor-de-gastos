import interfaz_cli as inter



# Funciones de ejecución

def ejec_bucle_pricipal():
    while True:
        inter.ver_titulo()
        inter.ver_menu_opcion()
        opcion = inter.solicitar_opcion()    # 1 = Gestiones | 2 = Reportes | None = Entrada inválida/fallida
        if opcion == 0:
            inter.ver_mensaje_salida()
            inter.esperar_continuar()
            inter.limpiar_consola()
            break
        elif opcion == 1:
            inter.ver_menu_gestion()
            gestion = inter.solicitar_gestion()
            if gestion == 0:
                inter.ver_mensaje_salida()
                inter.esperar_continuar()
                inter.limpiar_consola()            
                break
            elif gestion == 1.1:
                ejec_form_entrada()
            elif gestion == 1.2:
                ejec_form_salida()
            elif gestion == 1.3:
                pass # Ejecutar formulario de recurrencia - Pendiente
            elif gestion == 2.1:
                pass # Ejecutar formulario de modificacion  - Pendiente
            elif gestion == 2.2:
                pass # Ejecutar formulario de modificacion  - Pendiente
            elif gestion == 2.3:
                pass # Ejecutar formulario de modificacion  - Pendiente
            elif gestion == 3.1:
                pass # Ejecutar formulario de modificacion  - Pendiente
            elif gestion == 3.2:
                pass # Ejecutar formulario de modificacion  - Pendiente
            elif gestion == 3.3:
                pass # Ejecutar formulario de modificacion  - Pendiente
            else:
                continue
        elif opcion == 2:
            reporte = inter.ver_menu_reporte()
            if reporte == 0:
                inter.ver_mensaje_salida()
                inter.esperar_continuar()
                inter.limpiar_consola()            
                break
            elif reporte == 1.1:
                pass

        else:
            continue
        

## Formularios

def ejec_form_entrada():
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto = "", importe = "" , fecha_efectiva = "", recurrencia = "", nota = "")
    concepto = inter.solicitar_concepto()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto, importe = "" , fecha_efectiva = "", recurrencia = "", nota = "")
    importe = inter.solicitar_importe()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva = "", recurrencia = "", nota = "")
    fecha_efectiva = inter.solicitar_fecha_efectiva()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva, recurrencia = "", nota = "")
    recurrencia = inter.solicitar_recurrencia()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva, recurrencia, nota = "")
    nota = inter.solicitar_nota()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva, recurrencia, nota)
    inter.solicitar_confirmacion()

def ejec_form_salida():
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto = "", importe = "" , fecha_efectiva = "", recurrencia = "", nota = "")
    concepto = inter.solicitar_concepto()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto, importe = "" , fecha_efectiva = "", recurrencia = "", nota = "")
    importe = inter.solicitar_importe()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva = "", recurrencia = "", nota = "")
    fecha_efectiva = inter.solicitar_fecha_efectiva()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva, recurrencia = "", nota = "")
    recurrencia = inter.solicitar_recurrencia()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva, recurrencia, nota = "")
    nota = inter.solicitar_nota()
    inter.limpiar_consola()
    inter.ver_formulario_salida(concepto , importe , fecha_efectiva, recurrencia, nota)
    inter.solicitar_confirmacion()

## Selección

  
def ejec_gestiones(operacion):
    if operacion == 1.1:
        inter.limpiar_consola()
        ejec_form_entrada()
    elif operacion == 1.2:
        inter.limpiar_consola()
        ejec_form_salida()


ejec_bucle_pricipal()   