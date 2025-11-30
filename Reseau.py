
from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords
           
    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return False
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat
               
    def valider_reseau(self) -> bool:
    # 1. L’entrée doit être définie et exister
        if self.noeud_entree not in self.noeuds:
            return False
        
    # 2. Tous les nœuds doivent être connectés à au moins un arc
        for n in self.noeuds.keys():
            connecte = False

            for (a, b) in self.arcs:
                if n == a or n == b:
                    connecte = True
                    break
            if not connecte:
                return False
        return True
    

    def valider_distribution(self, t: Terrain) -> bool:
        clients=t.get_clients()
        for  c in range(len(clients)) :
            if not (clients[c] in self.noeuds.values()) :
               return False
        return True 

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)



    def afficher(self, t: Terrain) -> None:
        h, w = t.hauteur, t.largeur

        H, W = h * 2 - 1, w * 2 - 1
        grille = [[" " for _ in range(W)] for _ in range(H)]
        pos_affichage = {}
        for nid, (x, y) in self.noeuds.items():
            gx = x * 2      
            gy = y * 2      
            pos_affichage[nid] = (gx, gy)
            if nid == self.noeud_entree:
                grille[gx][gy] = "E"  
            elif t[x][y] == Case.CLIENT:
                    grille[gx][gy] = "C"
            elif t[x][y] == Case.OBSTACLE:
                grille[gx][gy] = "T"
            else:
                grille[gx][gy] = "+"   

        for n1, n2 in self.arcs:
            x1, y1 = pos_affichage[n1]
            x2, y2 = pos_affichage[n2]

            if x1 == x2:
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    if grille[x1][y] == " ":
                        grille[x1][y] = "-"
            elif y1 == y2:
                for x in range(min(x1, x2) + 1, max(x1, x2)):
                    if grille[x][y1] == " ":
                        grille[x][y1] = "|"

        for ligne in grille:
            print("".join(ligne))

                 

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("~", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout

