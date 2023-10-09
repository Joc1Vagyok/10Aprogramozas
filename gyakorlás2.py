"""str="Egy, megérett a megy.Kettő,csipke bokor vessző.Három, te vagy az én párom."
c=0
for i in range(len(str)):
    if (str[i]=="." or str[i]=="!" or str[i]=="?"):
        c+=1
if(c>1):
    print("Több mondatból áll")
else:
    print("Nem áll több mondatból")"""
lista=[
    ["Béla","f","18:00"],
    ["Júlia","n","18:01"],
    ["Zoli","t","18:05"],
]
for i in range(len(lista)):
    print(lista[:])

