
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        noeuds = {}
        arcs = []
        next_id = 0

        print("=== Mode de configuration manuelle du réseau ===")
        print("Tapez 'stop' pour arrêter.")

        # Choix de l'entrée sur le terrain
        print("\nCoordonnées de l'entrée (trouvées dans le terrain) :", t.get_entree())
        entree_coords = t.get_entree()
        if entree_coords == (-1, -1):
            print("Erreur : aucune entrée trouvée dans le terrain.")
            return -1, {}, []

        noeud_entree = next_id
        noeuds[noeud_entree] = entree_coords
        next_id += 1

        # Boucle principale : ajout de noeuds
        while True:
            print("\n--- Affichage actuel du réseau ---")
            self._afficher_temporaire(t, noeuds, arcs)

            cmd = input("Ajouter un nœud ? (o/n) : ").strip().lower()
            if cmd == "n" or cmd == "stop":
                break

            # Saisie du nœud
            print("\nEntrez les coordonnées du nœud (ex : '3 4') : ")
            tmp = input("> ").split()
            if len(tmp) != 2:
                print("Coordonnées invalides.")
                continue
            x, y = map(int, tmp)

            if not (0 <= x < t.hauteur and 0 <= y < t.largeur):
                print("Coordonnées hors terrain.")
                continue

            # Ajout du nœud
            nid = next_id
            noeuds[nid] = (x, y)
            next_id += 1

            print(f"Nœud {nid} ajouté en {x,y}")

            # Ajout d'arcs avec voisins existants
            print("Nœuds disponibles :", list(noeuds.keys()))
            while True:
                choix = input(f"Relier {nid} à quel nœud ? (id ou 'stop') : ")

                if choix == "stop":
                    break

                try:
                    autre = int(choix)
                except:
                    print("Entrez un numéro valide.")
                    continue

                if autre not in noeuds:
                    print("Nœud inexistant.")
                    continue

                arc = tuple(sorted((nid, autre)))
                if arc not in arcs:
                    arcs.append(arc)
                    print(f"Arc {arc} ajouté.")
                else:
                    print("Arc déjà existant.")

        return noeud_entree, noeuds, arcs

    # Petite fonction interne d'affichage temporaire pour aider l'utilisateur
    def _afficher_temporaire(self, t: Terrain, noeuds, arcs):
        grille = [[" " for _ in range(t.largeur)] for _ in range(t.hauteur)]

        # arcs
        for n1, n2 in arcs:
            (x1, y1) = noeuds[n1]
            (x2, y2) = noeuds[n2]

            if x1 == x2:
                for y in range(min(y1, y2)+1, max(y1, y2)):
                    grille[x1][y] = "-"
            elif y1 == y2:
                for x in range(min(x1, x2)+1, max(x1, x2)):
                    grille[x][y1] = "|"

        # noeuds
        for nid, (x,y) in noeuds.items():
            grille[x][y] = "E" if nid == 0 else str(nid)

        for ligne in grille:
            print("".join(ligne))

        
class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []

