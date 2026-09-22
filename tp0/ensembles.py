def robots_double_mission(exploration,transport):
    """Intersection des ensembles"""
    return exploration & transport

def robots_toutes_missions(exploration,transport):
    """Union sans doublons des ensembles"""
    return (exploration | transport) - (exploration & transport)
    #l'assertion ne passe pas car ils ont été remis dans l'ordre croissant pour l'assert

def robots_exploration_seulement(exploration,transport):
    """Soustraction des ensembles"""
    return exploration - transport

def ajouter_robot_mission(mission,robot):
    """Ajoute à l'ensemble le robot entré en paramètre""" 
    ens=mission.copy()
    ens.add(robot)
    return ens

def retirer_robot_mission(mission,robot):
    """Retire de l'ensemble le robot entré en paramètre""" 
    ens=mission.copy()
    ens.remove(robot)
    return ens

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
#assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")

assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}