import os

color_dict = {
    "red": "196",
    "green": "149",
    "orange": "208"
}

# METHODS ================================= #

def printf(content, color):
    color_code = color_dict[color]
    color_code = color_code + "m"
    to_print_start = "\033[38;5;"
    to_print_end = "\033[m"
    to_print = to_print_start + color_code + content + to_print_end
    print(to_print)

def get_printf_str(content, color):
    color_code = color_dict[color]
    color_code = color_code + "m"
    to_print_start = "\033[38;5;"
    to_print_end = "\033[m"
    to_print = to_print_start + color_code + content + to_print_end
    return to_print

def switch_case(content):
    global path

    content = content[1:]
    if content == "exit":
        sure_str = get_printf_str("¿Seguro que quieres acabar el proceso? - [y/N]", "orange")
        sure = input(sure_str)
        if sure == "y":
            print()
            printf("Saliendo...", "orange")
            exit()

    elif content == "help":
        print('''
               Uso de esta Tool

               /convert - Convierte de .ui a .py
               /help - Da este texto
               /exit - Cierra la tool

               ~ Created by: Laelaps ~
               (github.com/lae-laps) - For contact
               ''')
        return True

    elif content == "convert":
        new_name_str = get_printf_str("Nuevo nombre del fichero (con extensión .py): ", "orange")
        name = input(new_name_str)
        os.system("pyuic5 -x " + path + " -o " + name)
        print()
        printf("El fichero se convirtió a .py", "green")
        print()
        mv_org_str = get_printf_str("¿Mover .py a directorio original? ~ [y/N]", "orange")
        mv_org = input(mv_org_str)
        if mv_org == "y":
            path_to_mv = path.split("/")
            path_to_mv.pop()
            final_path = "/".join(path_to_mv)
            os.system("mv " + name + " " + final_path)
        return True

    else:
        return False


printf("===========", "green")
printf(".UI ==> .PY", "green")
printf("===========", "green")
print()

path_in_string = get_printf_str("Path absoluto del fichero .ui: ", "green")
path = input(path_in_string)

print()
printf("Usa /help para ver como se usa la tool", "green")
print()

# MAIN ========================================= #

while True:
    in_exe_str = get_printf_str("[/usr/lib] ~$ ", "green")
    exe = input(in_exe_str)
    is_instruction = switch_case(exe)
    if is_instruction == False:
        printf("~ Ese comando no existe ~ Usa '/help' para ver los comandos", "red")
        continue
