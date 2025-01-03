class Movie:
    platform = "Netflix"
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
    
    def __str__(self):
        return f"Filme: {self.name}"

    def techinalSheet(self):
        print("### Dados do Filme ###")
        print(f"Plataforma: {Movie.platform}")
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Nota do filme: {self.totalEvaluation}")
        print(f"Duração do Filme: {self.durationMinutes}")
        print(f"Total de Avaliadores: {self.evaluators}")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators +=1
    
    def avarage(self):
        print(f"Média do Filme {self.name}: {self.totalEvaluation / self.evaluators}\n")
        
mario = Movie("Super Mario Bros", 2023, False, 135)
avatar = Movie("Avatar", 2023, False, 180)

mario.evaluate(8)
mario.evaluate(10)
mario.techinalSheet()
mario.avarage()

# Mudando a plataforma
Movie.platform = "Prime Video"
avatar.evaluate(9.3)
avatar.evaluate(8.7)
avatar.techinalSheet()
avatar.avarage()