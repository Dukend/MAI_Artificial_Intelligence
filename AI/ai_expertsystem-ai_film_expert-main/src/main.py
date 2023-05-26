from expert_system import ExpertSystem
from rules import Rules
from database import FinalRules

def selectFinalRules():
    selectedFinalRules = []
    print("Фильмы каких жанров вы хотите посмотреть?\n"
          "Доступные жанры:")
    
    genre = []
    for k, v in enumerate(FinalRules):
        print(f"{k+1} : {v}")
        genre += [v]
    print("Например: '1 3' - выведет вам фильмы жанров комедия и боевик")
    selected = map(lambda x: int(x) - 1, input().split(' '))
    for num in selected:
        selectedFinalRules += FinalRules[genre[num]]
    return selectedFinalRules

if __name__ == '__main__':
    # Настраиваем экспертную систему
    selectedFinalRules = selectFinalRules()
    print('-'*10,'\n')

    # Запускаем экспертную систему
    es = ExpertSystem(Rules)
    es.run(selectedFinalRules)
    