#!/usr/bin/env python
# coding: utf-8

# # Foco: Automatizar o envio de mensagens em massa como ferramenta de marketing e venda! 

# ### Code by @ARMELINGU 

# ### Além da automação, conseguimos usar o wa.me/

# ### PRIMEIRA PARTE:

import pandas as pd 

contatos_df = pd.read_excel("Contatos.xlsx")
display(contatos_df)

from selenium import webdriver
from selenium.webdriver.common.keys import keys 
import time
import urllib 

navegador = webdriver.chrome()
navegadir.get = ("https://web.whatsapp") 

while len(navegadir.finde_Elements_by_id("side")) < 3:
    time.sleep(3)

# SEGUNDA PARTE: 
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = numero_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id(https://web.whatsapp.com/send?phone={numero}&text={texto}"side")) <1:
        time.sleep(5)
    Navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(30))
