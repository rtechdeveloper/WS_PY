import os
'''
arquivo para apagar arquivos _snd e _rcv de uma pasta system do TSS
'''
#informando o caminho da pasta
file_path = 'C:/TOTVS1233/TOTVSSPED/SYSTEM'

#listar os arquivos da pasta
file_list = os.listdir(file_path)

#verificando o arquivo e tamanho da pasta
for file in file_list:
    #guardando o caminho + nome do arquivo
    file_detail = f'{file_path}/{file}'
    
    size_file = os.path.getsize(file_detail) / 1000 #tamanho em megas
    
    #regra para apagar/mover arquivos
    if size_file < 1000:
        print(file, size_file)