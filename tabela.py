'''1. **Criação de Frases:**
    - Use variáveis de diferentes tipos e formate uma frase com os três métodos de formatação.
-----------------------------------------------------------------------------------------------'''

'''

name = "chuchene"
nume = 17

formata1 = f"Jogador de volei:{name}, idade:{nume}"

formata2 = "Jogador de volei:{}, idade:{}".format(name,nume)

formata3 = "Jogador de volei:%s, idade:%d" % (name,nume)

print(f"{formata1:<10s}\n{formata2:<10s}\n{formata3:<10}")

'''

'''-----------------------------------------------------------------------------------------------
2. **Tabela de Produtos:**
    - Dado um dicionário com informações de vários produtos, formate uma tabela exibindo nome, preço e quantidade de cada produto.
-----------------------------------------------------------------------------------------------'''

'''

dicio = [
    {"produto":"computador", "preço":10000, "site": "aliexpress" },
    {"produto":"iphone", "preço":5000, "site": "shoppe" },
    {"produto":"console", "preço":3000, "site": "amazon" }
]

indice = 0

while indice<len(dicio):
    item = dicio[indice]
    print(f"{item['produto']:<13} {item['preço']:<13.3f} {item['site']:<13}")
    indice += 1

'''

'''-----------------------------------------------------------------------------------------------
3. **Mensagens Personalizadas:**
    - Usando f-strings, crie uma mensagem para cada aluno em uma lista de dicionários, mostrando suas notas e se foram aprovados (nota >= 6) ou reprovados.
-----------------------------------------------------------------------------------------------'''

'''

alunos = [
    {"aluno":"Thiago", "nota": 9},
    {"aluno":"Pedro", "nota": 8},
    {"aluno":"Otavio,", "nota": 6},
    {"aluno":"Henrique", "nota": 4}
]

indice = 0

while indice < len(alunos):
    item = alunos[indice]
    if item['nota']<=6:
        print(f"{item["aluno"]:<10} {item["nota"]:<10} Você reprovou de ano estude mais para passar!! :(")
    else:
        print(f"{item["aluno"]:<10} {item["nota"]:<10} Você passou de ano!! :)")
    indice += 1

'''