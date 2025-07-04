def get_grde(score:int)->int:
    if 90<=score<=100:
        return "A"
    elif 60<=score<=89:
        return "B"
    elif 30<=score<=59:
        return "C"
    elif 0<=score<=29:
        return "F"
    else:
        return "1 dan 100 gacha kirting"
print(get_grde(int(input("son "))))