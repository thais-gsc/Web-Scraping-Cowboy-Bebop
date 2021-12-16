from bs4 import BeautifulSoup
import requests, lxml, time

html = requests.get("https://www.imdb.com/title/tt1267295/reviews?sort=submissionDate&dir=desc&ratingFilter=0")

html.encoding = html.apparent_encoding

html = html.text

soup = BeautifulSoup(html, "lxml")

reviews = soup.find_all(class_="text show-more__control")

comentarios = []

for review in reviews:
    texto = review.getText()
    comentarios.append(texto)

lista_palavras = []
lista_palavras_boas = []
lista_palavras_ruins = []

contador_bom = 0
contador_ruim = 0

for comentario in comentarios:
    # print(comentario)
    palavras = comentario.split()
    #print(palavras)
    for i in range(len(palavras)):
        lista_palavras.append(palavras[i])
        if palavras[i] == "fun" or palavras[i] == "good" or palavras[i] == "great" or palavras[i] == "incredible":
            lista_palavras_boas.append(palavras[i])
        elif palavras[i] == "bad" or palavras[i] == "horrible" or palavras[i] == "trash" or palavras[i] == "lame":
            lista_palavras_ruins.append(palavras[i])


ratings = soup.find_all(class_="rating-other-user-rating") 

notas = []

for rating in ratings:
    n = rating.getText()
    notas.append(n)

soma_nota = 0
for nota in notas:
    nota = nota.split()
    for n in nota:
        n = n.split("/")
        soma_nota += int(n[0])

contador_positivo = "Contador positivo: " + str(len(lista_palavras_boas))
contador_negativo = "Contador negativo: " + str(len(lista_palavras_ruins))
media = "Media: " + str(soma_nota/(len(notas)))

arquivo = open("cowboy_bebop.txt", "a")

texto = ""
texto += time.ctime() + "\n"
texto += contador_positivo + "\n"
texto += contador_negativo + "\n"
texto += media + "\n\n"

arquivo.write(texto)

arquivo.close()