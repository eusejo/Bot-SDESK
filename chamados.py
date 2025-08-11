from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from sys import argv
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('LOGIN_SDESK_USER')
password = os.getenv('LOGIN_SDESK_PASSWORD')

chrome = webdriver.Chrome()
descricao = 'Por favor, realizar a inspeção dos seguintes equipamentos especificados acima e identificar o estado do próprio.'

servico = int(argv[1])
equipa = argv[2]

equipamentos = {
    'D' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[1]/span/input',
    'M' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[2]/span/input',
    'N' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[3]/span/input',
    'No' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[4]/span/input'
}

def patri():
    patris = []
    with open('patri.txt','r') as arq:
        for c in arq.readlines():
            patris.append(int(c.strip()))
    return patris

def login(user, password):
    chrome.get('https://sdeskcloud.com.br/index.php?noAUTO=1')
    chrome.maximize_window()
    login = chrome.find_element(By.ID, "login_name").send_keys(user)
    user_password = chrome.find_element(By.ID, "login_password").send_keys(password)
    botao = chrome.find_element(By.NAME, 'submit')
    botao.click()
    sleep(1)
    criar_chamado()
    
def criar_chamado():
    chrome.get('https://sdeskcloud.com.br/marketplace/formcreator/front/formdisplay.php?id=5')
    sleep(1)
    
    selecionar = chrome.find_element(By.XPATH, r'/html/body/div[2]/div/div/main/div[1]/form/ol/li[1]/div[2]/div/div/div/select')
    opcoes = Select(selecionar)
    opcoes.select_by_index(servico)
    sleep(0.5)
    if servico == 1 or 3 or 4:
        inspecoes()

def inspecoes():
    equipamento = chrome.find_element(By.XPATH, rf'{equipamentos.get(equipa)}').click()

    patris = str(patri())
    patrimonio = chrome.find_element(By.XPATH, r'/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[3]/div/div/input').send_keys(patris.strip('[]'))

    descri = chrome.find_element(By.XPATH, r'/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[5]/div/div/input').send_keys(descricao)

    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)

    enviar = chrome.find_element(By.NAME, 'add')
    enviar.click()
    sleep(1)
    
login(user,password)