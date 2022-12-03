import chromedriver_binary # Abrir chromedriver sem o .exe
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from datetime import datetime
from time import sleep
import pandas as pd

link = 'http://broadcast.com.br/cadernos/financeiro/'

df = pd.DataFrame(columns=['categoria', 'data', 'titulo', 'texto'])


options = Options() # Options para o navegador
#options.add_argument('--headless')
options.add_argument('window-size=800,800')

def hora_atual():
    return datetime.now().strftime('%d/%m/%y %I:%M:%S')

def click(xpath): # click pelo xpath
    browser.find_element(By.XPATH, xpath).click()
    sleep(1)
    
def get_text(xpath): # pegando o texto pelo xpath
    return browser.find_element(By.XPATH, xpath).text
    
browser = webdriver.Chrome(options=options)

print('\n'+hora_atual()+'\n')

browser.get(link)
sleep(2)

#Aceitando cookies
click('/html/body/div[1]/div/a[1]')
sleep(1)

# Pegandos a 1 primeira materia
titulo = get_text('/html/body/div[3]/div[1]/div/div[1]')
texto = get_text('/html/body/div[3]/div[1]/div/div[2]')
conteudo = titulo+'\n'+texto

for i in range(1,4): 
    # Pegandos primeira filera de materias
    titulo = get_text(f'/html/body/div[3]/div[2]/div[{i}]/div[1]')
    texto = get_text(f'/html/body/div[3]/div[2]/div[{i}]/div[2]')
    conteudo = conteudo + titulo+'\n'+texto
    
    # Pegandos segunda filera de materias
    titulo = get_text(f'/html/body/div[3]/div[3]/div[{i}]/div[1]')
    texto = get_text(f'/html/body/div[3]/div[3]/div[{i}]/div[2]')
    conteudo = conteudo + titulo+'\n'+texto  
    sleep(1) 

# Limpando e transformqando e lista o conteudo
conteudo = conteudo.replace('continuar lendo', '')
conteudo = conteudo.split('\n')

while len(conteudo)!=1: # Passando conteudo para o dataframe
    df.loc[len(df)] = [conteudo[0].strip(), conteudo[1].strip(), conteudo[2].strip(), conteudo[3].strip()]
    del[conteudo[0]]
    del[conteudo[0]]
    del[conteudo[0]]
    del[conteudo[0]]
    print('COLETA FEITA!!!')
 
# Adicionando data da coleta
df=df.assign(data_atualizacao=hora_atual()) 
print(df)     

df.to_csv("conteudo.csv", encoding='UTF-8', index=False) #Salvando em .cs

browser.close()# Fechando naveaza