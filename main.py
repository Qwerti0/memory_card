class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3
        self.count_asked = 0
        self.count_right = 0

    def got_right(self):
        self.count_asked += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_asked += 1
        
    
question = [
    Question('Яка столиця ІрландіЇ?🚢🌏🗽','Дублін','Корк','Белфаст','Париж'),
    Question('Як перекладається Музика на англійську?🎵🎧🎙️','music','mysika','mouse','mysuca'),
    Question('Скільки буде 56+34 🎲🗿🛠️?','90','100','80','110'),
    Question('Який колір вийде якщо змішати синій з жовтим?💙💛✅','зелений','поморанчевий','червоний','фіолетовий'),
    Question('Що використовується в мові Python для написання тексту?🖥️📲📥','print','input','class','def')
]
