
from Terrain import Terrain, Case
from itertools import chain
import math
class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def ajouter_arc_automatique(self, noeuds_valides, num_noeud):
        arc=[]
        for n in noeuds_valides.keys() :
            if n != num_noeud :
                d = math.sqrt(
                    (noeuds_valides[n][0] - noeuds_valides[num_noeud][0])**2 +
                    (noeuds_valides[n][1] - noeuds_valides[num_noeud][1])**2
                    )
                if d==1 : 
                    arc.append((n,num_noeud))
        return arc
        
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds_valides={}
        arc = []
        noeuds_valides[0]=t.get_entree()
        select=0
        num_noeud=1
        while select != 3  :
            print("============================================================================")
            print("============================================================================")
            print("==========Noeuds disponibles====================")
            print(noeuds_valides)
            print("Affichege des noeud sur le terrain :")
            for ligne, l in enumerate(t.cases):
                for colonne, c in enumerate(l):
                    if (ligne, colonne) in noeuds_valides.values():
                        print(f"v", end="")
                    else:
                        if c == Case.OBSTACLE:
                            print("X", end="")
                        elif c == Case.CLIENT:
                            print("C", end="")
                        elif c == Case.VIDE:
                            print("~", end="")
                        elif c == Case.ENTREE:
                            print("E", end="")
                        else:
                            print(" ", end="")
                print()
            print("============================================================================")
            print("==========Arcs disponibles====================")
            print(arc)
            print("============================================================================")
            print("=== 1-Ajouter un noeud \n===2-Ajouter un arc \n=== 3-'Exit' pour terminer : ")
            select=int(input("===Votre choix : "))

            if select == 1 :
                print("===Ajouter une serie de noeuds automatiquement ? \n=== 1-Oui \n=== 2-Non")
                auto=int(input("===Votre choix : "))
                if auto == 1 :
                    print("===En ligne ou en colonne ? \n=== 1-Ligne \n=== 2-Colonne")
                    ligne_colonne=int(input("===Votre choix : "))
                    if ligne_colonne == 1 :
                        x=int(input("===Coordonnée Colone du noeud de départ : "))
                        y_start=int(input("===Coordonnée Ligne du noeud de départ : "))
                        y_stop=int(input("===Coordonnée Ligne du noeud de fin : "))
                        if y_start > y_stop :
                            q=y_start
                            y_start=y_stop
                            y_stop=q
                        for y in range(y_start, y_stop+1) :
                            noeuds_valides[num_noeud]=(y,x)
                            new_arc=self.ajouter_arc_automatique(noeuds_valides, num_noeud)
                            if len(new_arc)>0 :
                                for a in range(len(new_arc)) :
                                    arc.append(new_arc[a]) 
                            num_noeud+=1
                        print(f"===Noeuds de ({y_start},{x}) à ({y_stop},{x}) ajoutés avec succès.")
                    elif ligne_colonne == 2 :
                        y=int(input("===Coordonnée Ligne du noeud de départ : "))
                        x_start=int(input("===Coordonnée Colone du noeud de départ : "))
                        x_stop=int(input("===Coordonnée Colone du noeud de fin : "))
                        if x_start > x_stop :
                            q=x_start
                            x_start=x_stop
                            x_stop=q
                        for x in range(x_start, x_stop+1) :
                            noeuds_valides[num_noeud]=(y,x)
                            new_arc=self.ajouter_arc_automatique(noeuds_valides, num_noeud)
                            if len(new_arc)>0 :
                                for a in range(len(new_arc)) :
                                    arc.append(new_arc[a])                       
                            num_noeud+=1
                        print(f"===Noeuds de ({y},{x_start}) à ({y},{x_stop}) ajoutés avec succès.")
                        
                elif auto == 2 :
                    x=int(input("===Coordonnée Colone du noeud : "))
                    y=int(input("===Coordonnée Ligne du noeud : "))
                    noeuds_valides[num_noeud]=(y,x)
                    print(f"===Noeud {num_noeud}:({y,x}) ajouté avec succès.")
                    for n in noeuds_valides.keys() :
                        if n != num_noeud :
                            d = math.sqrt(
                                (noeuds_valides[n][0] - noeuds_valides[num_noeud][0])**2 +
                                (noeuds_valides[n][1] - noeuds_valides[num_noeud][1])**2
                                    )
                            if d==1 : 
                                print(f"===Voulez-vous ajouter l'arc ({n},{num_noeud}) ? \n=== 1-Oui \n=== 2-Non")
                                w=int(input("===Votre choix : "))
                                if w == 1 :
                                    arc.append((n,num_noeud))
                                    print(f"===Arc ({n},{num_noeud}) ajouté avec succès.")
                    num_noeud+=1
            elif select == 2 :
                add=False
                while add==False :
                    start=int(input("===Numéro du noeud de départ : "))
                    stop=int(input("===Numéro du noeud de fin : "))
                    if start in noeuds_valides.keys() and stop in noeuds_valides.keys() :
                        est_proche=math.sqrt((noeuds_valides[start][0]-noeuds_valides[stop][0])**2 +(noeuds_valides[start][1]-noeuds_valides[stop][1])**2)
                        if est_proche == 1 :
                            arc.append((start,stop))
                            print(f"===Arc ({start},{stop}) ajouté avec succès.")
                            add=True
                        else :
                            print("===Les noeuds ne sont pas adjacents, arc non ajouté.")
                            print("===1-Veuillez réessayer \n===2-Quitter sans ajouter d'arc")
                            w=int(input("===Votre choix : "))
                            if w == 2 :
                                add=True
        Entre_out=0               
        for s in noeuds_valides.keys() :
            if noeuds_valides[s] == t.get_entree() :
                Entre_out=s  
        return Entre_out, noeuds_valides, arc

class StrategieReseauAuto(StrategieReseau):
    def calcul_noeuf(self,terrain, client, client_test, save_nbx, taille, noeuds):
        if client[1] - client_test[1] < 0:
            start_x = client[1]
            start_y = client[0]
            stop_x  = client_test[1]
            stop_y  = client_test[0]
        else:
            start_x = client_test[1]
            start_y = client_test[0]
            stop_x  = client[1]
            stop_y  = client[0]

        for str_x in range(start_x, stop_x+1):
            noeuds_ram = []
            nbr_x = 0

            for n in range(start_x, str_x):
                noeuds_ram.append((start_y, n))

            if start_y < stop_y:
                for str_y in range(start_y, stop_y+1):
                    noeuds_ram.append((str_y, str_x))
            else:
                for str_y in range(start_y, stop_y-1, -1):
                    noeuds_ram.append((str_y, str_x))

            for d in range(str_x+1, stop_x+1):
                noeuds_ram.append((stop_y, d))

            for k in range(len(noeuds_ram)):
                if terrain[noeuds_ram[k][0]][noeuds_ram[k][1]] == Case.OBSTACLE:
                    nbr_x += 2
                else:
                    nbr_x += 1

            if (nbr_x < save_nbx) or (nbr_x == save_nbx and len(noeuds_ram) < taille):
                taille = len(noeuds_ram)
                save_nbx = nbr_x
                noeuds = noeuds_ram
        #print(noeuds)
        return noeuds, save_nbx, taille
    
    
    
    
    
    def configurer(self, terrain: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int,int]]]:
        noeuds_valides={}
        arc = []
        point=[]
        noeuds_valides[0]=terrain.get_entree()
        point.append(terrain.get_entree())
        point_valides=[]
        for i in range(len(terrain.get_clients())) :
            point.append(terrain.get_clients()[i])
        #print(point)
        
        p=0
        for i in range(len(point)):
            noeuds=[]
            client=point[i]
            client_tests=[]
            save_nbx=terrain.hauteur + terrain.largeur
            taille=terrain.hauteur * terrain.largeur
            
            if i !=0 :
                client_tests=point_valides.copy()
            
            for h in range(len(point)) :
                if (point[h] != point[i]):
                    client_tests.append(point[h])

                    
            client_tests = list(dict.fromkeys(noeuds_valides.values()))
            for j in range(len(client_tests)) : 
                client_test=client_tests[j]
                noeuds, save_nbx, taille = self.calcul_noeuf(terrain, client, client_test, save_nbx, taille, noeuds)                
            c=False
            ni=0
            #print(client_tests)
            for ne in range(len(noeuds)) :
                if not( tuple(noeuds[ne]) in noeuds_valides.values()):
                    noeuds_valides[ni+p]=tuple(noeuds[ne])
                    ni+=1
                elif (tuple(noeuds[ne]) in noeuds_valides.values() ) :
                    c=True
                    #print("ok")

            point_valides=list(chain(point_valides,noeuds))
            p=len(noeuds_valides)
            d=0
            d_save=terrain.hauteur * terrain.largeur
            save_noeud1=[0,0]
            save_noeud2=[0,0]
            noeu=[]
            if (not c) and (i !=0):
                for u in range(len(noeuds)) :
                    for v in noeuds_valides.values() :
                        d=math.sqrt((v[0]-noeuds[u][0])**2 +(v[1]-noeuds[u][1])**2)
                        if (d_save>d) and (client != v ):
                            d_save=d
                            save_noeud1=v
                            save_noeud2=noeuds[u]
                #print(save_noeud1,'     ',save_noeud2)
                noeu, save_n, tail = self.calcul_noeuf(terrain, save_noeud1, save_noeud2, terrain.hauteur * terrain.largeur,terrain.hauteur * terrain.largeur, noeuds)
                taille+=tail
                save_nbx +=save_n
                c=True 
                #print(noeu)  
            for n in range(len(noeu)) :
                noeuds_valides[n+p]=tuple(noeu[n])
            p=len(noeuds_valides)
            #print('-',noeu)
            noeuds=list(chain(noeuds,noeu))
                    
                
            
            #print (f'le meilleur pour : {client} et il est connecté à E : {c}',)
            #print(noeuds)
            #print("\n")       
        for s in noeuds_valides.keys() :
            for e in range(s+1,len(noeuds_valides)) :
                d = math.sqrt(
                    (noeuds_valides[s][0] - noeuds_valides[e][0])**2 +
                    (noeuds_valides[s][1] - noeuds_valides[e][1])**2
                        )
                if d==1 : 
                    arc.append((s,e))
        Entre_out=0
        for s in noeuds_valides.keys() :
            if noeuds_valides[s] == terrain.get_entree() :
                Entre_out=s
        return Entre_out,noeuds_valides, arc

