def quantite_piece(dictionnaire,modele,piece):
    """Retourne la quantite de pièces pour un modèle"""
    return dictionnaire[modele][piece]

def consommer_piece(dictionnaire,modele,piece,nb):
    """Soustrait le nombre d'une certaine pièce"""
    dictionnaire[modele][piece] -= nb

def ajouter_modele(dictionnaire,modele,moteurs,capteurs,roues):
    """Ajoute un modèle"""
    dictionnaire[modele] = {}
    dictionnaire[modele]["moteurs"]=moteurs
    dictionnaire[modele]["capteur"]=capteurs
    dictionnaire[modele]["roues"]=roues

def total_pieces(dictionnaire):
    """Donne le total des pièces tout modèle confondu"""
    texte = {}
    nb_moteurs=0
    nb_capteurs=0
    nb_roues=0
    for i in dictionnaire[modele]:
        nb_moteurs += dictionnaire[i]["moteurs"]
        nb_capteurs += dictionnaire[i]["capteurs"]
        nb_roues = dictionnaire[i]["roues"]
    texte["moteurs"]=nb_moteurs
    texte["capteurs"] = nb_capteurs
    texte["roues"] =nb_roues

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
ajouter_modele(pieces_stock, "ModeleC",
moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}
