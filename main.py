import matplotlib.pyplot as plt


def afficher_courbe_lineaire(
    pente: float,
    ordonnee_origine: float,
    x_min: float = -10,
    x_max: float = 10,
    nb_points: int = 100,
) -> None:
    if x_min >= x_max:
        raise ValueError("x_min doit être inférieur à x_max.")
    if nb_points < 2:
        raise ValueError("nb_points doit être au moins égal à 2.")

    pas = (x_max - x_min) / (nb_points - 1)
    x = [x_min + i * pas for i in range(nb_points)]
    y = [pente * valeur_x + ordonnee_origine for valeur_x in x]

    plt.plot(x, y, label=f"y = {pente:g}x + {ordonnee_origine:g}")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Courbe linéaire")
    plt.grid(True)
    plt.legend()
    plt.show()


def main() -> None:
    pente = float(input("Saisissez la pente (a) : "))
    ordonnee_origine = float(input("Saisissez l'ordonnée à l'origine (b) : "))
    afficher_courbe_lineaire(pente, ordonnee_origine)


