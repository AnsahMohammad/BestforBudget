databasePencil = [
    ["Pencil",1,20,4.5],["PencilXD",3,25,4.9],["PencilDas",7,13,4.0],["Pencil47",2,117,4.3]
]
# database pencil = name,code,price,rating

rating = 1
budget = 20

k = []

for i in databasePencil:
    if i[2]<= budget:
        k.append(i)

print(k)