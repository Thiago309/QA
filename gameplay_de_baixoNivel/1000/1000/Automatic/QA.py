from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

####################################################################

# Caminho para o seu arquivo HTML local
pagina_local = "file:///C:/Users/karer/OneDrive/Documentos/GitHub/QA/gameplay_de_baixoNivel/1000/1000/index.html"

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(pagina_local)
time.sleep(2)  # Aguarda carregamento da página

# Lista de testes
testes = [
    {
        "nome": "", "usuario": "", "senha": "", "senha2": "",
        "descricao": "Todos os campos vazios"
    },
    {
        "nome": "1234@!#", "usuario": "usuarioTeste", "senha": "senha123", "senha2": "senha123",
        "descricao": "Nome com caracteres inválidos"
    },
    {
        "nome": "NomeMuitoMuitoLongoMesmo", "usuario": "usuario1", "senha": "12345678", "senha2": "12345678",
        "descricao": "Nome com mais de 20 caracteres"
    },
    {
        "nome": "João Silva", "usuario": "usuario1", "senha": "123", "senha2": "123",
        "descricao": "Senha com menos de 8 caracteres"
    },
    {
        "nome": "João Silva", "usuario": "usuario2", "senha": "12 34 56", "senha2": "12 34 56",
        "descricao": "Senha com espaços"
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
    driver.find_element(By.ID, "name").clear()
    time.sleep(1)
    driver.find_element(By.ID, "username").clear()
    time.sleep(1)
    driver.find_element(By.ID, "password").clear()
    time.sleep(1)
    driver.find_element(By.ID, "password_2").clear()
    time.sleep(1)

    # Preencher campos
    driver.find_element(By.ID, "name").send_keys(teste["nome"])
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys(teste["usuario"])
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(teste["senha"])
    time.sleep(1)
    driver.find_element(By.ID, "password_2").send_keys(teste["senha2"])
    time.sleep(1)

    # Se for um teste de limpeza
    if teste.get("limpar", False):
        print(" Limpando campos após preenchimento...")
        time.sleep(1)
        driver.find_element(By.ID, "name").clear()
        time.sleep(1)
        driver.find_element(By.ID, "username").clear()
        time.sleep(1)
        driver.find_element(By.ID, "password").clear()
        time.sleep(1)
        driver.find_element(By.ID, "password_2").clear()
        time.sleep(1)
        print(" Campos limpos.\n")
    else:
        print(f" Dados inseridos: Nome='{teste['nome']}', Usuário='{teste['usuario']}', Senha='{teste['senha']}', Confirmar='{teste['senha2']}'\n")

    time.sleep(3)  # Espera final para observação

# Executa os testes
for teste in testes:
    preencher_e_validar(teste)

print(" Todos os testes foram executados.")
driver.quit()
