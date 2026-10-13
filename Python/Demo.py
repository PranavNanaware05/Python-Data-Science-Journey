numbers = [10, 20, 30, 20, 40, 10, 50]

for i in range(len(numbers)):
    flg=0
    for j in range(len(numbers)):
        if(i!=j and numbers[i]==numbers[j]):
            flg=1
            break

    if(flg==1):
     print(numbers[i])
