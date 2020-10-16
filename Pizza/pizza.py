#Mostra as musicas em uma pasta
#Você pode selecionar qual musica quer tocar.
import os
import pyglet

def menu_music(dire_musica):
    c = 0
    dic_musica = {}
    lista_musicas = os.listdir(dire_musica)    
    for arquivo in lista_musicas:
        if arquivo.endswith('.mp3'):
            c += 1
            dic_musica[c] = arquivo
    escolha_fin = sele_music(dic_musica)
    iniciar_music(dire_musica, escolha_fin)
    

def sele_music(dic_musica):
    for arquivo in dic_musica:
        print(f'({arquivo}) {dic_musica[arquivo]}')
    escolha = int(input('Qual música?'))
    escolha_fin = dic_musica[escolha]
    return escolha_fin


def iniciar_music(dire_musica, escolha_fin):
    musica_dir = f'{dire_musica}/{escolha_fin}'
    music = pyglet.media.load(musica_dir)
    music.play()
    pyglet.app.run()

dire_musica = '/home/gustavoad/Documents/Certificados/Musicas'
menu_music(dire_musica)
