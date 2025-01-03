'''
1 - O método estático não utiliza o parâmetro referente a classe.
2 - O método estático pode acessar, mas não pode modificar o estado da classe.
3 - Usamos o decorator @staticmethod para criar um método de classe.
'''

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
        
    @staticmethod
    def courses_trail(trail):
        if trail == "Python":
            courses = ["Python", "Django", "Flask"]
        elif trail == "Java":
            courses = ["JPA", "Spring", "Hibernate"]
        elif trail == "C#":
            courses = ["C#", "ASP.NET", "SignalR"]
        else:
            courses = ["A definir"]
        return courses
    
print(Course.courses_trail("Python"))