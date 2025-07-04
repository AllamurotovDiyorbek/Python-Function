def is_valid_iphone_number(phone:str)->bool:
    if len(phone)==9 and phone.isdigit():
        return True
    else:
        return False
