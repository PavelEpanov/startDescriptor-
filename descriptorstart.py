class AgeDesc:
    def __get__(self, instance, owner):
        return 40
    def __set__(self, instance, value):
        instance._age = value
class descriptors():
    age = AgeDesc()

x = descriptors()
x.age # Запускается AgeDesk.__get__
# 40
x.age = 42 # Запускается AgeDesk.__set__
x._age # Нормальное извлечение: AgeDesc не вызывается 
# 42
