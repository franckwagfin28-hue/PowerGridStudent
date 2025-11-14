
from Terrain import Terrain,Case
from Reseau import Reseau
from itertools import chain
from StrategieReseau import StrategieReseauManuelle

if __name__ == "__main__":

    reseau = Reseau()
    terrain = Terrain()
    terrain.charger("terrains/t2.txt")
    print("Terrain chargé :")
    terrain.afficher()
    print("======= Configuration Automatique")
    reseau.configurer(terrain)
    largeur = terrain.largeur
    hauteur = terrain.hauteur
    noeuds_valides={}
    arc = []
    Noeuds=[]
    point=[]
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
        good_noeud=[]
        
        if i !=0 :
            client_tests=point_valides.copy()
        
        for h in range(len(point)) :
            if (point[h] != point[i]):
                client_tests.append(point[h])
        print(client_tests)
            #for h in range(len(point)) :
                
        #client_tests = list(dict.fromkeys(client_tests))
        for j in range(len(client_tests)) : 
            client_test=client_tests[j]
            #print(client_test)
            if client[1] - client_test[1] < 0:
                start_x=client[1]
                start_y=client[0]
                stop_x=client_test[1]
                stop_y=client_test[0]
            else :
                start_x=client_test[1]
                start_y=client_test[0]
                stop_x=client[1]
                stop_y=client[0]
            for str_x in range(start_x,stop_x+1):  
                noeuds_ram=[]
                nbr_x=0
                for n in range(start_x,str_x) :
                    noeuds_ram.append((start_y,n))

                if start_y<stop_y : 
                    for str_y in range(start_y,stop_y+1) :
                        noeuds_ram.append((str_y,str_x))
                else :
                    for str_y in range(start_y,stop_y-1 , -1) :
                        noeuds_ram.append([str_y,str_x])  
                for d in range(str_x+1,stop_x+1) : 
                    noeuds_ram.append((stop_y,d)) 
                for k in range(len(noeuds_ram)) :
                    if terrain[noeuds_ram[k][0]][noeuds_ram[k][1]] == Case.OBSTACLE :
                        nbr_x +=1
                # if point[1]==client : 
                #     print(nbr_x,'         ',taille,'        ', len(noeuds_ram))
                #     print(nbr_x < save_nbx , (len(noeuds_ram)<=taille))

                if  (nbr_x < save_nbx) or (nbr_x == save_nbx and len(noeuds_ram) < taille):
                    taille=len(noeuds_ram)
                    #print(taille)
                    save_nbx=nbr_x
                    noeuds.clear()
                    noeuds=noeuds_ram
                            # if noeuds_ram[0] != client :
                            #     nex_out=noeuds_ram[0]
                            # else :
                            #     nex_out=noeuds_ram[-1]                 
        for n in range (len(noeuds)) :
            noeuds_valides[n+p]=noeuds[n]
        point_valides=list(chain(point_valides,noeuds))
        print(point_valides)
        print(noeuds)
        print ('le meilleur pour',client)
        p=len(noeuds_valides)
        print(noeuds)
        print('\n\n\n')
            # for h in (client[1]) :
            #     for l in (client[0]):
            #         if terrain[h][l] == Case.OBSTACLE:
            #                 print("X", end="")
            #         if terrain[h][l] == Case.CLIENT:
            #                 print("C", end="")
            #         if terrain[h][l] == Case.VIDE:
            #                 print("~", end="")
            #         if terrain[h][l] == Case.ENTREE:
            #                 print("E", end="")
            #         else:
            #             print(" ", end="")
            #         print("")

    if reseau.valider_reseau() and reseau.valider_distribution(terrain):
        print("Configuration valide simple trouvée")
        print("Cout : {}M€".format(reseau.calculer_cout(terrain)))
        reseau.afficher_avec_terrain(terrain)
    else:
        print("Pas de configuration valide trouvée.")

    print("======= Configuration Manuelle")
    reseau.set_strategie(StrategieReseauManuelle())
    reseau.configurer(terrain)
    if reseau.valider_reseau() and reseau.valider_distribution(terrain):
        print("Configuration valide optimale trouvée")
        print("Cout : {}M€".format(reseau.calculer_cout(terrain)))
        reseau.afficher_avec_terrain(terrain)
    else:
        print("Pas de configuration valide optimale trouvée.")


