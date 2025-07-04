def is_strong_password(password:str):
    if len(password)>8:
        return "Kuchli"
    elif len(password)==0:
        return "Bosh maydon"
    else:
        return "kuchsiz"