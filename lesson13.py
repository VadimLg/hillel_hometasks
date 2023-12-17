class NotEquality:
    def __init__(self, text):
        self.text = text

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        elif abs(len(self.text) - len(other.text)):
            print(f"Довжина рядка \"{self.text}\" не дорівнює довжині рядка \"{other.text}\"")
            return True
        else:
            print(f"Довжина рядка \"{self.text}\" дорівнює довжині рядка \"{other.text}\"")
            return False


str_1 = NotEquality("Привіт")
str_2 = NotEquality("Хай!")
str_3 = NotEquality("Hello!")

print("Визначення нерівності довжини (не рівне - True, рівне - False)")

print(("Позитивний кейс:"))
print(str_1 != str_2)

print(("Негативний кейс:"))
print(str_1 != str_3)
