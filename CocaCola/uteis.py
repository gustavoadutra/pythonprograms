import os
import os.path
import shutil


def arq_sel(dir_busca, dir_final, tam_bytes):
    print('=='*20)
    pic_folder(dir_busca, dir_final, tam_bytes)


def pic_folder(dir_busca, dir_final, tam_bytes):
    #Variáveis:
    dir_lista = os.listdir(dir_busca)
    img_tupla = ('jpg', 'png', 'jpeg', 'peg')
    for arq_in in dir_lista:
        if arq_in.endswith(img_tupla):
            print(f'\033[1;32m"{arq_in}" é uma imagem.\033[0;0m')
            arq_intam = os.stat(dir_busca + arq_in).st_size
            if arq_intam >= tam_bytes:
                try:
                    shutil.copy(dir_busca + arq_in, dir_final)
                except PermissionError:
                    print('Permissão negada.')
                    continue
                else:
                    print('O arquivo foi copiado com sucesso.')
            else:
                print('\033[1;91mO arquivo possui uma qualidade muito ruim.\033[0;0m')

        elif os.path.isdir(dir_busca + arq_in) and not arq_in.endswith('.BIN'):
            print('=='*20)
            print(f'\033[1;33m"{arq_in}" é uma pasta.\033[0;0m')
            arq_sel(dir_busca + arq_in + '/', dir_final, tam_bytes)
