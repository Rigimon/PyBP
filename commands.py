#
# Feito por: Rigimon
#

import os
import shutil
import webbrowser

PATH = os.getcwd()
PATH_PASS = PATH + r"\data\pass.txt"
PATH_KEEP_PASS = PATH + r"\data\password.txt"
PATH_CMD = PATH + r"\john\run"
PA = False

def pegar_item(PATH_ITEM):
    global PATH_CMD, PA
    
    try:
        PATH_ITEM = PATH_ITEM.replace("/","\\")
        item = PATH_ITEM.split("\\")[-1]
        NEW_PATH_ITEM = PATH_CMD + "\\" + item
        if PATH_ITEM != NEW_PATH_ITEM:
            shutil.copy(PATH_ITEM, NEW_PATH_ITEM)
            PA = True
        return item
    except FileNotFoundError:
        with open(".\data\log.txt", "a+") as arq:
            arq.write('file error')
    except FileExistsError:
        return item
    except Exception:
        with open(".\data\log.txt", "a+") as arq:
            arq.write('Erro Inesperado')

def descobrir_senha(item):
    
    global PATH_CMD, PATH_PASS, PA
    ext = item[-item[::-1].find("."):]
    VER_SENHA = ext + "2john.exe " + item + "> hash.txt"
    QUEBRAR_SENHA = "john.exe hash.txt> " + PATH_PASS
    SALVAR_SENHA = "john.exe -show hash.txt> " + PATH_PASS

    os.chdir(PATH_CMD)
    os.system(VER_SENHA)
    os.system(QUEBRAR_SENHA)
    os.system(SALVAR_SENHA)
    with open(PATH_PASS,"r") as arq:
            texto = arq.readlines()
    if PA == True:
        os.remove(PATH_CMD + "\\" + item)

def consulta(item):
    global PATH_PASS
    texto = ""
    with open(PATH_PASS,"r") as arq:
        texto = arq.readlines()
    if item in texto[0]:
        return texto[0]
    #if "No password hashes left to crack" in texto[len(texto)-1]:
        #os.system("john.exe -show hash.txt> " + PATH_PASS)
        #with open(PATH_PASS,"r") as arq:
        #    texto = arq.readlines()
    if 'No password hashes loaded' in texto[len(texto)-1] or "0 password hashes cracked" in texto[0]:
        return item + ":sem senha"
    else:
        return texto[0]

def guardar_senha(texto):
    global PATH_KEEP_PASS
    save = False
    with open(PATH_KEEP_PASS,"r") as arq:
        txt = arq.readlines()
        for i in txt:
            if texto == i:
                save = True
                break
    if not save:
        with open(PATH_KEEP_PASS,"a") as arq:
            arq.write(texto)
                
def consul():
    global PATH_KEEP_PASS
    with open(PATH_KEEP_PASS,"r") as arq:
        txt = arq.readlines()
    return txt

def comparar_itens(item):
    txt = consul()
    for senha in txt:
        if item in senha:
            return senha
    return False

def feedback(url):
    webbrowser.open(url)
