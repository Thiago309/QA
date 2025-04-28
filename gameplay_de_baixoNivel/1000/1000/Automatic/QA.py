from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Caminho para o seu arquivo HTML local
pagina_local = "file:///C:/Users/karer/OneDrive/Documentos/GitHub/QA/gameplay_de_baixoNivel/1000/1000/index.html"
# pagina_local = "file:///C:/Users/thiago.vsantos/Documents/GitHub/QA/gameplay_de_baixoNivel/1000/1000/index.html"

# Inicializar navegador
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get(pagina_local)

time.sleep(2)  # Aguarda carregamento da página

# Clicando nos icones de olho, para mostrar a senha
listaOlhos = navegador.find_elements("class name", "toggle-visibility")

for botao in listaOlhos:
    if "👁️" in botao.text:
        botao.click()
        time.sleep(0.5)
        
# Lista de testes
testes = [
    {
        "senha": "", "senha2": "",
        "descricao": "Todos os campos vazios"
    },
    {
        "senha": "sen123", "senha2": "sen123",
        "descricao": "Senha com quantidade de caracteres abaixo do minimo requisitado."
    },
    {
        "senha": "123456789", "senha2": "987654321",
        "descricao": "Senhas diferentes"
    },
    {
        "senha": "senhalongamasmuitolongamesmo", "senha2": "senhalongamasmuitolongamesmo",
        "descricao": "Senha com mais de 16 caracteres"
    },
    {
        "nome": "Limpar", "usuario": "teste", "senha": "limpo123", "senha2": "limpo123",
        "descricao": "Campos preenchidos e depois limpos",
        "limpar": True
    },
]

# Função de preenchimento
def preencher_e_validar(teste):
    print(f" Iniciando: {teste['descricao']}")
    time.sleep(1)

    # Limpar os campos
    navegador.find_element(By.ID, "password").clear()
    time.sleep(1)
    navegador.find_element(By.ID, "password_2").clear()
    time.sleep(1)

    # Preencher campo senha letra por letra
    campo_senha = navegador.find_element(By.ID, "password")
    for i in range(len(teste["senha"])):
        campo_senha.send_keys(teste["senha"][i])
        time.sleep(0.2)  # Simula digitação humana

    time.sleep(1)

    # Preencher campo senha2 letra por letra
    campo_senha2 = navegador.find_element(By.ID, "password_2")
    for i in range(len(teste["senha2"])):
        campo_senha2.send_keys(teste["senha2"][i])
        time.sleep(0.2)  # Simula digitação humana

    time.sleep(1)
    
    # Se for um teste de limpeza
    if teste.get("limpar", False):
        print(" Limpando campos após preenchimento...")
        navegador.find_element(By.ID, "password").clear()
        time.sleep(1)
        navegador.find_element(By.ID, "password_2").clear()
        time.sleep(1)
        print(" Campos limpos.\n")
    else:
        print(f" Dados inseridos: Senha='{teste['senha']}', Confirmar='{teste['senha2']}'\n")

    time.sleep(2)  # Espera final para observação

# Executa os testes
for teste in testes:
    preencher_e_validar(teste)

botao_login = navegador.find_element(By.ID, "cadastrarBtn")
botao_login.click()

print(" Todos os testes foram executados.")
navegador.quit()