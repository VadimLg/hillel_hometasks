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


obj_str_1 = NotEquality("Привіт")
obj_str_2 = NotEquality("Хай!")
obj_str_3 = NotEquality("Hello!")

print("Визначення нерівності довжини (не рівне - True, рівне - False)")

print(("Позитивний кейс:"))
print(obj_str_1 != obj_str_2)

print(("Негативний кейс:"))
print(obj_str_1 != obj_str_3)
