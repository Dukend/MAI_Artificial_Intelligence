from database import FilmSamples
from util import getAns

class Content():
    def __init__(self, x):
        self.x = x

class AND(Content):
    pass

class OR(Content):
    pass

class Ask(Content):
    def __init__(self, question):
        self.question = question
        
    def ask(self) :
        return getAns(self.question)

class ExpertSystem():
    def __init__(self, rules):
        self.rules = rules
        self.memory = {}
    
    def run(self, facts):
        was = False
        for fact in facts:
            # print(f'узнаю подходит ли поджанр {fact}')
            res = self.get(fact)
            if res == 'Да':
                was = True
                print(f"Я думаю, что тебе стоит посмотреть что-то в поджанре {fact}")
                print("Фильмы, которые я рекомендую:")
                for k, v in enumerate(FilmSamples[fact]):
                    print(f"{k+1} : {v}")
                    
                ans = getAns("Продолжить подбирать поджанры?")
                if ans == 'Нет':
                    break
        if not was:
            print("К сожалению, мы не смогли что-то подобрать для вас\n")

    def get(self, fact):
        # Ответ уже есть
        if fact in self.memory.keys():
            return self.memory[fact]
        # Нужно вывести Ответ
        if fact not in self.rules:
            print(f"Ошибка. Мы не нашли факта в словаре правил: {fact}\n")
            exit()
        res = self.handleExpr(self.rules[fact])
        self.memory[fact] = res
        return res

    def handleExpr(self, expr):
        # Если выражение Ask
        if isinstance(expr, Ask):        
            return expr.ask()
        # Если выражение And
        elif isinstance(expr, AND):
            for op in expr.x:
                if self.get(op) == 'Нет':
                    return 'Нет'
            return 'Да'
        # Если выражение Or
        elif isinstance(expr, OR):
            for op in expr.x:
                if self.get(op) == 'Да':
                    return 'Да'
            return 'Нет'
