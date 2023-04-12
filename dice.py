import random 

quest = input("Quer jogar um dado?") 

response = "y"

while response:
    no = random.randint(1,6)

    if no == 1:
        print("[---]")
        print("[   ]")
        print("[ 1 ]")
        print("[   ]")
        print("[---]")
    if no == 2:
        print("[---]")
        print("[   ]")
        print("[ 2 ]")
        print("[   ]")
        print("[---]")
    if no == 3:
        print("[---]")
        print("[   ]")
        print("[ 3 ]")
        print("[   ]")
        print("[---]")
    if no == 4:
        print("[---]")
        print("[   ]")
        print("[ 4 ]")
        print("[   ]")
        print("[---]")
    if no == 5:
        print("[---]")
        print("[   ]")
        print("[ 5 ]")
        print("[   ]")
        print("[---]")
    if no == 6:
        print("[---]")
        print("[   ]")
        print("[ 6 ]")
        print("[   ]")
        print("[---]")

    quest = input("Digite y para continuar ou n para sair") 
