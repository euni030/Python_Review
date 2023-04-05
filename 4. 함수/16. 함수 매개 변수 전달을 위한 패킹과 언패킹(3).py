#패킹
def Print(**price):
    for key in price:
        print(key, ":", price[key])

Print(cola = 100, cider = 50, fanta = 70)


#언패킹
def Sum(cola, cider, fanta):
    return cola + cider + fanta

items = { "cola":100, "cider": 50, "fanta": 70 }
print(Sum(**items))    # 딕셔너리 언패킹 => Sum(cola=100, cider=50, fanta=70)
