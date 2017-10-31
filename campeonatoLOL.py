from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

url = 'http://br.lolesports.com/'

driver = webdriver.PhantomJS()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
divs = soup.findAll('div',{'class', 'esp-header-matches-matchlink'})

campeonato = []
for div in divs:
	partida = ""

	###############################################
	## aqui encontraremos os times que participaram da partida
	## para isso encontramos a imagem que contém os times e pegamos
	## apenas o seu título, que é o nome do time que procuramos
	## Armazenamos em uma lista, assim a posiçao 0 tem um time e a posição 1 tem outro
	timesDaPartida = []
	timesDiv = div.findAll('div',{'class', 'esp-header-matches-match__team'})
	for timeDiv in timesDiv:
		timesDaPartida.append(timeDiv.find('img', {'class', 'image-responsive'})['title'])
	###############################################

	###############################################
	## Aqui encontraremos o resultado de tal partida
	## Para isso, encontramos o parágrafo (p) que contém essa informação
	resultadoDiv = div.find('div',{'class', 'esp-header-matches-match__score'})
	resultadosP = resultadoDiv.findAll('p')
	resultado = ""
	for resultadoP in resultadosP:
		resultado += resultadoP.text

	resultado = resultado.split() 						#usamos essa função para retirar os espaços em branco da string	porém ela quebra a string
														# em duas partes (pontucao do primeiro time, pontuacao do segundo)

	pontuacao = resultado[0] + ' x ' + resultado[1]		#juntamos os dois valores novamente, agora sem os espaços em branco
														#coloquei um 'x' entre os números do resultado só pra ficar mais bonito mesmo
	###############################################


	#agora ja temos os times e a pontuação de cada um, podemos concatená-los numa mesma string 
	#para ter todas as informações necessárias da partida.
	partida = timesDaPartida[0] + ' ' + pontuacao + ' ' + timesDaPartida[1]	

	print(partida)
	campeonato.append(partida)
#print(campeonato)
