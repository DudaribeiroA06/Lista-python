lista_de_palavras =["geladeira","móvel","palmito", "morte", "peixe","poção","eduarda","caçar"]
maisde5=[palavra for palavra in lista_de_palavras if len(palavra)  > 5 ]
print(maisde5)