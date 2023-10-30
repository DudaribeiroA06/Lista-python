num = [2,5,10,11,22,50,3,7,1,8]
numMaior =0
numMenor = [0]
for x in num:
    if x>numMaior:
        numMaior = x
     print("O maior número da lista é" +  (numMaior))
    for x in num:
        if x<=numMenor:
             numMenor = x
        print("O menor número da lista é" + (num_Menor))
