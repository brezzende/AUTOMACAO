#processos do projeto
import time
import pandas as pd
import pyautogui

# Configurações do PyAutoGUI
pyautogui.PAUSE = 1  # Aumentar pausa entre comandos
pyautogui.FAILSAFE = True  # Manter fail-safe ativado por segurança

# Aguardar alguns segundos antes de começar
print("Iniciando automação em 5 segundos... Mova o mouse para um canto da tela para interromper.")
time.sleep(5)

#passo 1: abrir o sistema da empresa 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#passo 2: fazer login
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("pytonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenhaaqui")
pyautogui.press("tab")
pyautogui.press("enter")

#passo 3: importar base de dados dos produtos
#ler arquivo csv
tabela = pd.read_csv("produtos.csv")

#passo 4: cadastrar 1 produto 
for linha in tabela.index: 
    pyautogui.click(x=974, y=291)
    #codigo
    codigo=tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca=tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo=tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))

    pyautogui.press("tab")
    #categoria
    categoria=tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario= tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo
    custo=tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
   
    #obs
    obs=str(tabela.loc[linha, "obs"])
    if obs != "nan":   
        pyautogui.write(obs)
    pyautogui.press("tab")
    #apertar o botao de enviar
    pyautogui.press("enter")
    #passo 5: repetir todos os passos ate acabar todos os produto
    pyautogui.scroll(10000)
