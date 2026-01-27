import shutil
from typing import Final

# Constantes de marca (Single Source of Truth)
BRAND_NAME: Final[str] = "IACRIOLLA"
SLOGAN: Final[str] = "Inteligencia artificial con viveza criolla."

def iacriolla_banner() -> None:
    """
    Imprime la firma de marca optimizada para la terminal del proyecto.
    Detecta el ancho de la terminal para asegurar un renderizado limpio.
    """
    # Colores ANSI
    CYAN: Final[str] = "\033[1;36m"
    MAGENTA: Final[str] = "\033[1;35m"
    RESET: Final[str] = "\033[0m"

    # Obtener dimensiones de terminal o usar ancho por defecto del slogan
    term_width = shutil.get_terminal_size(fallback=(80, 20)).columns
    content_width = min(len(SLOGAN), term_width - 4)
    
    border = "=" * content_width
    
    # Renderizado
    print(f"{CYAN}{border}{RESET}")
    print(f"{MAGENTA}{BRAND_NAME.center(content_width)}{RESET}")
    print(f"{SLOGAN.center(content_width)}")
    print(f"{CYAN}{border}{RESET}")

if __name__ == "__main__":
    iacriolla_banner()
