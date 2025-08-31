print("--------MENU--------")
menu = {"aloo":10
        ,"paneer":15
        ,"bengan":11
        ,"khichdi":14
        }
for k , v in menu.items():
    print(f"{k:10}:{v}")
print("--------------------")
total = 0
order = []
while True:
    t = input("enter your item (q to quit): ")
    if menu.get(t) is not None:
        order.append(t)
        total += menu.get(t)
    elif t == "q":
        break
print("--------ORDER-------")
for i in order:
    print(f"{i:10}:{menu.get(i)}")

print(f"--------------------\ntotal     :{total}")