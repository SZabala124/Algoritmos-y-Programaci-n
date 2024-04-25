import time

# En Python no existen las constantes, pero por convensión, si una variable está toda en mayúscula, se considera una constante.

# Todas las constantes están en gramos (grs)

print("Bienvenid@ al tutorial del día de hoy para aprender a hacer arepas.")
time.sleep(3)

TAZA_AGUA = float(250)
TAZA_HARINA = float(120)
TAZA_SAL = float(540)
TAZA_ACEITE = float(225)

CDA_AGUA = float(15)
CDA_HARINA = 8.72
CDA_SAL = float(32)
CDA_ACEITE = 13.8

CDTA_AGUA = float(5)
CDTA_HARINA = 2.91
CDTA_SAL = float(9)
CDTA_ACEITE = 4.5

# variable initialization

terminar = False
cant_agua = None
unid_agua = None
cant_harina = None
unid_harina = None
cant_sal = None
unid_sal = None
cant_aceite = None
unid_aceite = None

unidad_deseada = None
factor_conversion = 1
cantidad_masa_total = 0

opcion_agua = "a) Agua\n"
opcion_harina = "b) Harina\n"
opcion_sal = "c) Sal\n"
opcion_aceite = "d) Aceite\n"
opcion_salir = "s) Salir del programa\n"

mensaje_inicial = 0
if terminar == 1:
    mensaje_inicial = 1
    if mensaje_inicial == 1:
        print("Bienvenid@ al tutorial del día de hoy para aprender a hacer arepas.")
        time.sleep(3)
        
pregunta_inicial = "\n¿Deseas añadir algún ingrediente?\n"

# Menú
while not terminar:
    message = pregunta_inicial
    if cant_agua is None or unid_agua is None:
        message += opcion_agua
    if cant_harina is None or unid_harina is None:
        message += opcion_harina
    if cant_sal is None or unid_sal is None:
        message += opcion_sal
    if cant_aceite is None or unid_aceite is None:
        message += opcion_aceite
    message += opcion_salir
    ingrediente_seleecionado = input(message)
    if ingrediente_seleecionado.lower() == "a" and (cant_agua is None or unid_agua is None):

        # Seleccionar la Unidad
        agua_selection = None
        while agua_selection is None or agua_selection.lower() != "s":
            agua_message = """\n
            Unidad deseada:
            a) Tazas
            b) Cdas
            c) Cdtas
            s) Volver al menú principal
            """
            agua_selection = input(agua_message)
            if agua_selection == "a":
                unid_agua = "tazas"
                break
            elif agua_selection == "b":
                unid_agua = "cdas"
                break
            elif agua_selection == "c":
                unid_agua = "cdtas"
                break
        if agua_selection != "s":
            # Seleccionar la Cantidad
            while not cant_agua:
                cant_agua = input(
                    """
                Cantidad deseada ("s" para salir): """
                )
                if cant_agua == "s":
                    cant_agua = None
                    break
                if not cant_agua.isdigit():
                    if "." in cant_agua:
                        tmp = cant_agua.replace(".", "")
                        if not tmp.isdigit():
                            cant_agua = None
                    else:
                        cant_agua = None

    elif ingrediente_seleecionado.lower() == "b" and (cant_harina is None or unid_harina is None):
        # Seleccionar la Unidad
        harina_selection = None
        while harina_selection is None or harina_selection.lower() != "s":
            harina_message = """\n
            Unidad deseada:
            a) Tazas
            b) Cdas
            c) Cdtas
            s) Volver al menú principal
            """
            harina_selection = input(harina_message)
            if harina_selection == "a":
                unid_harina = "tazas"
                break
            elif harina_selection == "b":
                unid_harina = "cdas"
                break
            elif harina_selection == "c":
                unid_harina = "cdtas"
                break
        if harina_selection != "s":
            # Seleccionar la Cantidad
            while not cant_harina:
                cant_harina = input(
                    """
                Cantidad deseada ("s" para salir): """
                )
                if cant_harina == "s":
                    cant_harina = None
                    break
                if not cant_harina.isdigit():
                    if "." in cant_harina:
                        tmp = cant_harina.replace(".", "")
                        if not tmp.isdigit():
                            cant_harina = None
                    else:
                        cant_harina = None
    elif ingrediente_seleecionado.lower() == "c" and (cant_sal is None or unid_sal is None):
        # Seleccionar la Unidad
        sal_selection = None
        while sal_selection is None or sal_selection.lower() != "s":
            sal_message = """\n
            Unidad deseada:
            a) Tazas
            b) Cdas
            c) Cdtas
            s) Volver al menú principal
            """
            sal_selection = input(sal_message)
            if sal_selection == "a":
                unid_sal = "tazas"
                break
            elif sal_selection == "b":
                unid_sal = "cdas"
                break
            elif sal_selection == "c":
                unid_sal = "cdtas"
                break
        if sal_selection != "s":
            # Seleccionar la Cantidad
            while not cant_sal:
                cant_sal = input(
                    """
                Cantidad deseada ("s" para salir): """
                )
                if cant_sal == "s":
                    cant_sal = None
                    break
                if not cant_sal.isdigit():
                    if "." in cant_sal:
                        tmp = cant_sal.replace(".", "")
                        if not tmp.isdigit():
                            cant_sal = None
                    else:
                        cant_sal = None
    elif ingrediente_seleecionado.lower() == "d" and (cant_aceite is None or unid_aceite is None):
        # Seleccionar la Unidad
        aceite_selection = None
        while aceite_selection is None or aceite_selection.lower() != "s":
            aceite_message = """\n
            Unidad deseada:
            a) Tazas
            b) Cdas
            c) Cdtas
            s) Volver al menú principal
            """
            aceite_selection = input(aceite_message)
            if aceite_selection == "a":
                unid_aceite = "tazas"
                break
            elif aceite_selection == "b":
                unid_aceite = "cdas"
                break
            elif aceite_selection == "c":
                unid_aceite = "cdtas"
                break
        if aceite_selection != "s":
            # Seleccionar la Cantidad
            while not cant_aceite:
                cant_aceite = input(
                    """
                Cantidad deseada ("s" para salir): """
                )
                if cant_aceite == "s":
                    cant_aceite = None
                    break
                if not cant_aceite.isdigit():
                    if "." in cant_aceite:
                        tmp = cant_aceite.replace(".", "")
                        if not tmp.isdigit():
                            cant_aceite = None
                    else:
                        cant_aceite = None
    elif ingrediente_seleecionado.lower() == "s":
        terminar = True
    if (
        cant_agua is not None
        and unid_agua is not None
        and cant_harina is not None
        and unid_harina is not None
        and cant_sal is not None
        and unid_sal is not None
        and cant_aceite is not None
        and unid_aceite is not None
    ):
        terminar = False
        break

if terminar:
    print("¡Hasta la próxima!")
    exit()

cant_agua = float(cant_agua)
cant_harina = float(cant_harina)
cant_sal = float(cant_sal)
cant_aceite = float(cant_aceite)

print("------------------------------------------------------------------------------------------------")
print(
    f"""
Tenemos lo siguiente:
    Agua:
        unidad: {unid_agua.title()}    cantidad: {cant_agua}
    Harina:
        unidad: {unid_harina.title()}  cantidad: {cant_harina}
    Sal:
        unidad: {unid_sal.title()}     cantidad: {cant_sal}
    Aceite:
        unidad: {unid_aceite.title()}  cantidad: {cant_aceite}
"""
)
time.sleep(3)

masa_seleccionada = None
while masa_seleccionada is None:
    masa_seleccionada = input(
        """\n
    Unidad de masa deseada:
    a) Kgs
    b) Grms
    s) Salir del programa
    """
    )
    if masa_seleccionada.lower() == "a":
        unidad_deseada = "kg"
        break
    elif masa_seleccionada.lower() == "b":
        unidad_deseada = "gr"
        break
    elif masa_seleccionada.lower() == "s":
        print("¡Hasta la próxima!")
        exit()
    else:
        masa_seleccionada = None

print(f"La unida a deseada es: {unidad_deseada}")
if unidad_deseada == "kg":
    factor_conversion = 1 / 1000

# Conversion agua
if unid_agua == "tazas":
    cant_agua *= TAZA_AGUA
elif unid_agua == "cdas":
    cant_agua *= CDA_AGUA
elif unid_agua == "cdtas":
    cant_agua *= CDTA_AGUA
else:
    print(f"¿¿¿QUE PASO AQUÍ???, como que no tengo la unidad de agua!!!!")
cant_agua *= factor_conversion

# Conversion harina
if unid_harina == "tazas":
    cant_harina *= TAZA_HARINA
elif unid_harina == "cdas":
    cant_harina *= CDA_HARINA
elif unid_harina == "cdtas":
    cant_harina *= CDTA_HARINA
else:
    print(f"¿¿¿QUE PASO AQUÍ???, como que no tengo la unidad de harina!!!!")
cant_harina *= factor_conversion

# Conversion sal
if unid_sal == "tazas":
    cant_sal *= TAZA_SAL
elif unid_sal == "cdas":
    cant_sal *= CDA_SAL
elif unid_sal == "cdtas":
    cant_sal *= CDTA_SAL
else:
    print(f"¿¿¿QUE PASO AQUÍ???, como que no tengo la unidad de sal!!!!")
cant_sal *= factor_conversion

# Conversion aceite
if unid_aceite == "tazas":
    cant_aceite *= TAZA_ACEITE
elif unid_aceite == "cdas":
    cant_aceite *= CDA_ACEITE
elif unid_aceite == "cdtas":
    cant_aceite *= CDTA_ACEITE
else:
    print(f"¿¿¿QUÉ PASO AQUÍ???, ¿CÓmo que no tengo la unidad de aceite?")
cant_aceite *= factor_conversion
cant_aceite *= 0.75

print("------------------------------------------------------------------------------------------------")
print(
    f"""
Tenemos lo siguiente:
    Agua:
        unidad: {unidad_deseada.title()+"s"}    cantidad: {cant_agua}
    Harina:
        unidad: {unidad_deseada.title()+"s"}   cantidad: {cant_harina}
    Sal:
        unidad: {unidad_deseada.title()+"s"}      cantidad: {cant_sal}
    Aceite:
        unidad: {unidad_deseada.title()+"s"}   cantidad: {cant_aceite}
"""
)
time.sleep(3)

cantidad_masa_total = cant_agua + cant_harina + cant_sal + cant_aceite
print(f"La cantidad de masa total es {cantidad_masa_total} {unidad_deseada.title() + 's'}")