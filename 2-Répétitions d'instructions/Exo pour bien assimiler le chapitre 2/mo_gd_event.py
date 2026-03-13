import locale, sys
from pathlib import Path

# locale.setlocale(locale.LC_ALL, "fr_FR")

# sys.path.append(str(Path(__file__).parent.parent.parent / "tools"))
# from pymox_kit import cls, end

try:
    from pymox_kit import cls, end
except Exception:
    # Fallback minimal si pymox_kit échoue (ex: locale fr_FR absente).
    def cls():
        import subprocess

        try:
            subprocess.run(["clear"], check=False)
        except Exception:
            print("\033[2J\033[H", end="")
        

    def end():
        print('\n')


def haut():
    print("↑", end=" ")


def bas():
    print("↓", end=" ")


def gauche():
    print("←", end=" ")


def droite():
    print("→", end=" ")

def exemple_1():
    cls()
    
    l=4 # Réduis la taille du problème, et quand ça marchera là, tu mettras 10 ici !
    
    for loop in range(l-1):
        haut()
    for loop in range(l-1):
        droite()
        bas()
    for loop in range(l-2):
        gauche()
        bas()
    for loop in range(l-2):
        droite()
        bas()
    for loop in range(l-2):
        gauche()
        bas()
    for loop in range(l-2):
        droite()
        bas()
    for loop in range(l-2):
        gauche()
        bas()
    for loop in range(l-2):
        droite()
        bas()
    for loop in range(l-2):
        gauche()
        bas()
    for loop in range(l-2):
        droite()
        bas()
    for loop in range(l-1):
        gauche()
    end()

if __name__ == "__main__":
    # Look ta CLI et prends une feuille de 4 cases X 4 cases, et tu verras vite le problème ! ;-) ! :
    exemple_1()
    
# -----------------------------------------------------------------------------------------------

# Dois-je te répéter exactement la même chose que la veille ?

# Ton résultat avec les chiffres en dur :

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ← ← ← ← ← ← ← ← 

# Avec la variable l=10 :

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ ← ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ → ↓ ← ← ← ← ← ← ← ← ←

# → Bref, le script avec la variable marche pareil.

# On réduit donc le problème avec l = 4, ce qui donne :

# ↑ ↑ ↑ → ↓ → ↓ → ↓ ← ↓ ← ↓ → ↓ → ↓ ← ↓ ← ↓ → ↓ → ↓ ← ↓ ← ↓ → ↓ → ↓ ← ↓ ← ↓ → ↓ → ↓ ← ← ←

# Ce script tourne dans un workspace, je t'en ai fait un PR :-) !

# https://prnt.sc/13TpwcM0Yy-r


# Prends une feuille de 4 cases X 4 cases, et tu verras vite le problème ! ;-) ! :

# Bon, c'est quand-même mieux que la veille ! :

# https://prnt.sc/1vzgQxTEcIb2