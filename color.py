from colorama import Fore, Back, Style, init
# Inicializar colorama
init(autoreset=True)

# Colores disponibles
VERDE = Fore.GREEN
ROJO = Fore.RED
AMARILLO = Fore.YELLOW
AZUL = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
BLANCO = Fore.WHITE
GRIS = Fore.LIGHTBLACK_EX

# Fondos
FONDO_ROJO = Back.RED
FONDO_VERDE = Back.GREEN
FONDO_AZUL = Back.BLUE

# Estilos
NEGRITA = Style.BRIGHT
NORMAL = Style.NORMAL
RESET = Style.RESET_ALL

# Funciones de utilidad
def titulo(texto):
    """Muestra un título en azul y negrita"""
    print(f"\n{FONDO_AZUL}{BLANCO}{NEGRITA}{'='*50}")
    print(f"{texto.center(50)}")
    print(f"{'='*50}{RESET}\n")

def exito(texto):
    """Muestra un mensaje de éxito en verde"""
    print(f"{VERDE}✓ {texto}{RESET}")

def error(texto):
    """Muestra un mensaje de error en rojo"""
    print(f"{ROJO}✗ {texto}{RESET}")

def advertencia(texto):
    """Muestra una advertencia en amarillo"""
    print(f"{AMARILLO}⚠ {texto}{RESET}")

def info(texto):
    """Muestra información en cyan"""
    print(f"{CYAN}ℹ {texto}{RESET}")

def menu_opcion(numero, descripcion):
    """Formatea una opción del menú"""
    print(f"{FONDO_AZUL}{BLANCO}{NEGRITA} {numero} {RESET} {MAGENTA}{NEGRITA}{descripcion}{RESET}")

def separador():
    """Muestra un separador"""
    print(f"{GRIS}{'─'*50}{RESET}")

def input_color(mensaje, color=CYAN):
    """Realiza un input con color"""
    return input(f"{color}{mensaje}{RESET}")
