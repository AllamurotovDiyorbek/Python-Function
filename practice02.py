def calculate_age(birth_year,current_year):
    if current_year-birth_year>=23:
        return "Siz balog`atga yetgansiz"
    elif current_year<birth_year:
        return "xatolik bor"
    else:
        return "Siz balog`atga yetmagansiz"
print(calculate_age(int(input("my birthday")),int(input("now"))))