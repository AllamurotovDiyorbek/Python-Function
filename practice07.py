savol="Bitta ota-onaning 4 o‘g‘li bor. Har bir o‘g‘ilning bir singlisi bor. Nechta bola bor?"
javob="5ta"
def ask_question(question:str,correct_answer:str):
    return question
def check_answer(user_answer,correct_answer):
    if correct_answer.lower()==user_answer.lower():
        return "Javob tog`ri"
    else:
        return "Javob notog`ri"
result=ask_question(savol,javob)
print(result)
a=input("kriting  faqat( ta) qoshimchasi bosin?  ")
print(check_answer(user_answer=a,correct_answer=javob))