# Antes de tudo: Baixar o python e antes de rodar o código instalar o SELENIUM e o WEBDRIVER_MANAGER via terminal.
# Quanto maior o tempo de intervalo entre os envios das mensagens, mais dificíl de tomar bloqueio.
# Lembre-se: WHATSAPP NÃO GOSTA DE AUTOMAÇÕES!!! 
# Código desenvolvido por @armelingu

# 1
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 

# 2
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# 3
contatos = ['adicionar contatos']
mensagem = 'Hello, World! Teste automação code by @armelingu'

#4
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(4)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER) 

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem) 
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos: 
    buscar_contato(contato)
    enviar_mensagem(mensagem)

