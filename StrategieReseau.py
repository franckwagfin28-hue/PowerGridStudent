
from Terrain import Terrain, Case
from itertools import chain
import math
class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []

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

        return noeuds, save_nbx, taille
    
    
    
    
    
    def configurer(self, terrain: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
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
            #print(client_tests)
                #for h in range(len(point)) :
                    
            #client_tests = list(dict.fromkeys(client_tests))
            for j in range(len(client_tests)) : 
                client_test=client_tests[j]
                noeuds, save_nbx, taille = self.calcul_noeuf(terrain, client, client_test, save_nbx, taille, noeuds)                
            c=0
            ni=0
            for ne in range(len(noeuds)) :
                if not( tuple(noeuds[ne]) in noeuds_valides.values()):
                    noeuds_valides[ni+p]=tuple(noeuds[ne])
                    ni+=1
                if (noeuds[ne] in noeuds_valides.values() ) :
                    c=True
                if c != True : c=False
            point_valides=list(chain(point_valides,noeuds))
            p=len(noeuds_valides)
            #print(noeuds)
            d=0
            d_save=terrain.hauteur * terrain.largeur
            save_noeud1=[0,0]
            save_noeud2=[0,0]
            noeu=[]
            if (not c) and (i !=0):
                for u in range(len(noeuds)) :
                    for v in noeuds_valides.values() :
                        d=math.sqrt((v[0]-noeuds[u][0])**2 +(v[1]-noeuds[u][1])**2)
                        if (d_save>d) :
                            d_save=d
                            save_noeud1=v
                            save_noeud2=noeuds[u]
                noeu, save_n, tail = calcul_noeuf(terrain, save_noeud1, save_noeud2, terrain.hauteur * terrain.largeur,terrain.hauteur * terrain.largeur, noeuds)
                taille+=tail
                save_nbx +=save_n
                c=True   
            for n in range(len(noeu)) :
                noeuds_valides[n+p]=tuple(noeu[n])
            p=len(noeuds_valides)
            #print('-',noeu)
                #noeuds=list(chain(noeuds,noeu))
                    
                
            
            #print (f'le meilleur pour : {client} et il est connecté à E : {c}',)
            #print("\n")       
        for s in noeuds_valides.keys() :
            for e in range(s+1,len(noeuds_valides)) :
                d = math.sqrt(
                    (noeuds_valides[s][0] - noeuds_valides[e][0])**2 +
                    (noeuds_valides[s][1] - noeuds_valides[e][1])**2
                        )
                if d==1 : 
                    arc.append((s,e))
        return 1,noeuds_valides, arc

