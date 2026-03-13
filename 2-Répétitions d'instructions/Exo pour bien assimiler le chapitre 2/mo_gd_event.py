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
    
    L = 4 # Réduis la taille du problème, et quand ça marchera là, tu mettras 10 ici !
    
    for colonne in range(L):
        if colonne % 2 == 0:
            for _ in range(L - 1):
                haut()  
        else:
            for _ in range(L - 1):
                bas()
        if colonne < L-1:
            droite()
        for _ in range(L - 1):
            gauche()
        
    end()

if __name__ == "__main__":
    # Look ta CLI et prends une feuille de 4 cases X 4 cases, et tu verras vite le problème ! ;-) ! :
    exemple_1()
    
# -----------------------------------------------------------------------------------------------

# Dois-je te répéter exactement la même chose que la veille ?

# Ton résultat :

# ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → ← ← ← ← ← ← ← ← ← ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ → ← ← ← ← ← ← ← ← ← ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → ← ← ← ← ← ← ← ← ← ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ → ← ← ← ← ← ← ← ← ← ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → ← ← ← ← ← ← ← ← ← ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ → ← ← ← ← ← ← ← ← ← ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → ← ← ← ← ← ← ← ← ← ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ → ← ← ← ← ← ← ← ← ← ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ → ← ← ← ← ← ← ← ← ← ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ← ← ← ← ← ← ← ← ←

# On réduit donc le problème avec L = 4, ce qui donne :

# ↑ ↑ ↑ → ← ← ← ↓ ↓ ↓ → ← ← ← ↑ ↑ ↑ → ← ← ← ↓ ↓ ↓ ← ← ← 

# Ce script tourne dans un workspace, je t'en ai fait un PR :-) !

# https://prnt.sc/vCuj6_sd024w


# Prends une feuille de 4 cases X 4 cases, et tu verras vite le problème ! ;-) ! :

# Et du coup, on voit bien que c'est pas mieux que la veille ! :-( :

# https://prnt.sc/5tCfRIS0yb1W