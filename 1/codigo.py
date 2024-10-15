#passo 1: entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "gabrielshow@gmail.com"
senha = "11132"

#pyautogui.write > escrever um texto
#pyautogui.click >  clicar com o mouse
#pyautogui.press > apertar uma tecla
#pyautogui.hotkey > apertar uma atalho (ctrl, C)
#pyautogui.PAUSE = 1

pyautogui.PAUSE = 0.5

# abrir o navegador 
    # ---- apertar a tecla WIN
pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")

# passo 2: fazer login

pyautogui.write(link) #faltou tempo ( deu erro de primeira )
pyautogui.press("enter")
#----- dar uma pausa de 3seg para o site abrir
time.sleep(3)
pyautogui.click(x=807, y=384) #varia com a res do monitor
pyautogui.write(email)
pyautogui.click(x=762, y=493) #ou usava TAB
pyautogui.write(senha)
pyautogui.press("enter")

time.sleep(2)

# passo 3: importar a base de dados
     #----Pandas (base de dados mais usado) pip install pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


# passo 4: cadastrar 1 produto

pyautogui.click(x=700, y=274)



linha = 0
#rodar em cada linha
for linha in tabela.index:
    pyautogui.press("home")
    pyautogui.click(x=700, y=274)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo" ]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #Preço unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs ]
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(1000)


# passo 5: Repetir processo de cadastro até acabar os produtos
