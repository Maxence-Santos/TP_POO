def afficher_releve(mesure):
    """Affiche les valeurs du tuple"""
    texte = f"Capteur {mesure[0]} : {str(mesure[1])} {mesure[2]}"
    return texte

def recalibrer(liste, capteur, val):
    """Modifie la valeur d'un capteur"""
    for i in range(len(liste)-1):
        liste[i] = list(liste[i])
        if liste[i][0] == capteur:
            liste[i][1] = val
            liste[i] = tuple(liste[i])
        break
    return liste

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]
assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3