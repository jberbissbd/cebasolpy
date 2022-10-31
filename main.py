from agents_interficie import ProjecteInterficie, ClientsInterficie


a = ProjecteInterficie()
b = ClientsInterficie()
llistat = []
llista_clients = []
for projecte in a.projectes:
    info_buscada = [projecte.id, projecte.data, projecte.codi, projecte.client.nom, projecte.tarifa.descripcio,
                    projecte.tipus.codi]
    llistat.append(info_buscada)
for clients in b.clients:
    info_buscada_clients = [clients.id,clients.codi,clients.nom]
    llista_clients.append(info_buscada_clients)
print(llistat)
print(llista_clients)




