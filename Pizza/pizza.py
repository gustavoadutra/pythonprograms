#Mostra as musicas em uma pasta
#Você pode selecionar qual musica quer tocar..
import os
dic_musica = {}
def org_music(dire_musica):
    lista_musicas = os.listdir(dire_musica)
    for arquivo in lista_musicas:
        if arquivo.endswith('.mp3'):
            for c in range(0, len(lista_musicas)):
                dic_musica[c] = arquivo    
    print(dic_musica)
    return dic_musica


def menu(dir_musica, dic_musica):
    print('MENUM')
    for arquivo, c in enumerate(dic_musica):
        print(arquivo, c)

dire_musica = 
dic_musica = org_music(dire_musica)
menu('/home/gustavoad/Documents/Certificados/Musicas', )
