from agents_interficie import ProjecteInterficie
a = ProjecteInterficie()
llistat = []
for projecte in a.projectes:
    info_buscada = [projecte.id,projecte.data,projecte.codi,projecte.client.nom,projecte.tarifa.descripcio,
                    projecte.tipus.codi]
    llistat.append(info_buscada)
print(llistat)





