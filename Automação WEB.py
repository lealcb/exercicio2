from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
url	= 'https://login.live.com/oauth20_authorize.srf?response_type=token&client_id=000000004C18365E&redirect_uri=https%3A%2F%2Fto-do.live.com%2Ftasks%2Fauth%2Fcallback&scope=https://graph.microsoft.com/User.Read&state=eyJ0b2tlblR5cGUiOiJncmFwaFRva2VuIiwiZmxvd1R5cGUiOiJtc2EifQ==&aadredir=1'

navegador	= Firefox()

navegador.get(url)
time.sleep(6)
elemento	= navegador.find_element_by_xpath("//input[@class='form-control ltr_override input ext-input text-box ext-text-box' and @name='loginfmt']")
elemento.click()
elemento.clear()
elemento.send_keys("leal.leal.bp@outlook.com")
botao_elemento	= navegador.find_element_by_id('idSIButton9')
botao_elemento.click()
time.sleep(5)
senha_elemento	= navegador.find_element_by_xpath("//input[@class='form-control input ext-input text-box ext-text-box' and @name='passwd']")
senha_elemento.click()
senha_elemento.clear()
senha_elemento.send_keys("Zelda@123")
botao_elemento	= navegador.find_element_by_id('idSIButton9')
botao_elemento.click()
time.sleep(5)
botao_elemento	= navegador.find_element_by_id('idSIButton9')
botao_elemento.click()
time.sleep(10)



def nova_tarefa(tarefa):
	nova_tarefa	= navegador.find_element_by_id('baseAddInput-addTask') # Adicionar a tarefa
	nova_tarefa.send_keys(tarefa) # Nome da tarefa
	nova_tarefa.send_keys(Keys.RETURN)
def nova_lista(lista):
	nova_lista	= navegador.find_element_by_id('baseAddInput-addList')
	nova_lista.send_keys(lista) #Criando o nome da Lista
	nova_lista.send_keys(Keys.RETURN) #Pressinando enter para colocar ela
	
nova_lista('Livros') 
validar_lista	=  navegador.find_element_by_xpath(f"//span[text()='Livros']") # Procura pela lista criada
validar_lista.click()
nova_tarefa('A arte da Guerra')
nova_tarefa('A Cauda Longa')
nova_tarefa('A Torre Negra')
validar_lista.click() 
validar_tarefa	= navegador.find_elements_by_xpath('//span[@class="checkBox big"]')
listando_livros	= navegador.find_elements_by_class_name("taskItem-title")
achando_importante = navegador.find_elements_by_xpath('//span[@class="importanceButton"]')
achando_importante[0].click()

#Validação


time.sleep(3)



try:
	achando_titulo_criado = navegador.execute_script(""" return Array.prototype.slice.call(document.getElementsByClassName("listItem-title listItem-titleParsed")).filter(function (x) { return x.textContent === "Livros";});""")
	assert len(achando_titulo_criado) == 1
	nome_correto = achando_titulo_criado[0].text
	validador = nome_correto == 'Livros'
	print(f"Lista foi criado? : {validador}")

except:
	print("Titulo não criado")

time.sleep(2)

achando_nome_criado	  = navegador.find_elements_by_xpath('//span[@class="taskItem-title"]')


nome1 = achando_nome_criado[0].text
nome2 = achando_nome_criado[1].text
nome3 = achando_nome_criado[2].text

print("Teste de Nomes criados: A Cauda Longa, A arte da Guerra, A torre Negra")
if nome2 == 'A Cauda Longa':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if nome3 == 'A arte da Guerra':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if nome1 == 'A Torre Negra':
	print("Teste: OK")
else:
	print("Teste: ERRO")

time.sleep(2)


validar_importante = achando_nome_criado[1].find_element_by_xpath('//span[@class="importanceButton color-theme"]')

try:
	validar_importante.find_element_by_xpath('//i[@class="icon fontIcon ms-Icon ms-Icon--FavoriteStarFill iconSize-20"]')
	print("A torre negra está como importante")
except:
	print("A torre negra não está como importante")




arq_listas_livros = open('livros.csv', 'r')
lista_livros = arq_listas_livros.read().split('\n')
arq_listas_livros.close()

livro1 = lista_livros[1]
livro2 = lista_livros[2]
livro3 = lista_livros[3]
livro4 = lista_livros[4]
livro5 = lista_livros[5]
livro6 = lista_livros[6]
livro7 = lista_livros[7]
livro8 = lista_livros[8]
livro9 = lista_livros[9]
livro10 = lista_livros[10]


nova_lista('Meus Livros')
nova_tarefa(f'{livro1}')
time.sleep(2)
nova_tarefa(f'{livro2}')
time.sleep(2)
nova_tarefa(f'{livro3}')
time.sleep(2)
nova_tarefa(f'{livro4}')
time.sleep(2)
nova_tarefa(f'{livro5}')
time.sleep(2)
nova_tarefa(f'{livro6}')
time.sleep(2)
nova_tarefa(f'{livro7}')
time.sleep(2)
nova_tarefa(f'{livro8}')
time.sleep(2)
nova_tarefa(f'{livro9}')
time.sleep(2)
nova_tarefa(f'{livro10}')

time.sleep(3)
validar_tarefa_ativa = navegador.find_element_by_xpath('//li[@class="listItem-container active"]')
validar_tarefa	= validar_tarefa_ativa.find_elements_by_xpath('//span[@class="checkBox big"]')
listando_livros	= validar_tarefa_ativa.find_elements_by_class_name("taskItem-title")
achando_checkbox	= validar_tarefa_ativa.find_elements_by_xpath('//span[@class="checkBox big"]')
achando_checkbox[0].click()
achando_checkbox	= validar_tarefa_ativa.find_elements_by_xpath('//span[@class="checkBox big"]')
achando_checkbox[1].click()
achando_importante = validar_tarefa_ativa.find_elements_by_xpath('//span[@class="importanceButton"]')
achando_importante[4].click()
achando_importante = validar_tarefa_ativa.find_elements_by_xpath('//span[@class="importanceButton"]')
achando_importante[5].click()
achando_importante = validar_tarefa_ativa.find_elements_by_xpath('//span[@class="importanceButton"]')
achando_importante[6].click()

try:
	achando_titulo_criado = navegador.execute_script(""" return Array.prototype.slice.call(document.getElementsByClassName("listItem-title listItem-titleParsed")).filter(function (x) { return x.textContent === "Meus Livros";});""")
	assert len(achando_titulo_criado) == 1

	nome_correto = achando_titulo_criado[0].text
	validador = nome_correto == 'Meus Livros'
	print(f"Lista foi criado? : {validador}")

except:
	print("Titulo não criado")

achando_nome_criado	  = validar_tarefa_ativa.find_elements_by_xpath('//span[@class="taskItem-title"]')


witcher = achando_nome_criado[0].text
dificil = achando_nome_criado[1].text
portugues = achando_nome_criado[2].text
ler = achando_nome_criado[3].text
viagem = achando_nome_criado[4].text
galaxia = achando_nome_criado[5].text
inteligencia = achando_nome_criado[6].text
sapiens = achando_nome_criado[7].text
scrum = achando_nome_criado[8].text
sherlock = achando_nome_criado[9].text
print("Teste de Nomes criados:")
if inteligencia == 'Como aprender inteligencia':
	print("Teste: OK")
else:
	print('Teste: ERRO')
if witcher == 'The Witcher: O último desejo':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if portugues == 'Guia pratico do portugues correto VOL 1':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if ler == 'Como Ler Livros':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if viagem == 'Esta não é mais uma historia sobre viagens no tempo':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if galaxia == 'Guia do mochilheiro da galaxia':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if dificil == 'O Lado Dificil das situaçoes dificeis':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if sapiens == 'Uma breve historia da humanidade: Sapiens':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if sherlock == 'Sherlock Holmes':
	print("Teste: OK")
else:
	print("Teste: ERRO")
if scrum == 'SCRUM a arte de fazer o dobro do trabalho pela metade do tempo':
	print("Teste: OK")
else:
	print("Teste: ERRO")


validar_importante = achando_nome_criado[8].find_element_by_xpath('//span[@class="importanceButton color-theme"]')

try:
	validar_importante.find_element_by_xpath('//i[@class="icon fontIcon ms-Icon ms-Icon--FavoriteStarFill iconSize-20"]')
	print("está como importante: OK")
except:
	print("ESTÁ COMO IMPORTANTE : ERRO ")

validar_importante = achando_nome_criado[1].find_element_by_xpath('//span[@class="importanceButton color-theme"]')

try:
	validar_importante.find_element_by_xpath('//i[@class="icon fontIcon ms-Icon ms-Icon--FavoriteStarFill iconSize-20"]')
	print("está como importante: OK")
except:
	print("ESTÁ COMO IMPORTANTE : ERRO ")

validar_importante = achando_nome_criado[0].find_element_by_xpath('//span[@class="importanceButton color-theme"]')

try:
	validar_importante.find_element_by_xpath('//i[@class="icon fontIcon ms-Icon ms-Icon--FavoriteStarFill iconSize-20"]')
	print("está como importante: OK")
except:
	print("ESTÁ COMO IMPORTANTE : ERRO ")
	

