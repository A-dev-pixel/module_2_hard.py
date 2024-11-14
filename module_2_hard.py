new=int(input("Введите число от 3 до 20: "))
rezult=[]
def number_new(new):
    for i in range(1,21):
        for j in range(1+i,21):
            if new % (j+i) == 0:
                rezult.append(i)
                rezult.append(j)
    return(rezult)
print(number_new(new))