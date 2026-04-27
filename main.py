# # 1
class Ovqat:
    def __init__(self, nomi):
        self.nomi = nomi

    def tayyorlash(self):
        print("Ovqat tayyorlandi")

class Palov(Ovqat):
    def tayyorlash(self):
        print("Palov tayyorlandi")

a = Palov("Osh")
a.tayyorlash()


# # 2
class Haydovchi:
    def __init__(self, ism):
        self.ism = ism

    def haydash(self):
        print("Haydayapti")

class TaksiHaydovchi(Haydovchi):
    def haydash(self):
        print("Yo‘lovchi tashimoqda")

a1 = Haydovchi("Ali")
a2 = TaksiHaydovchi("Vali")

a1.haydash()
a2.haydash()


# # 3
class Oyin:
    def __init__(self, nomi):
        self.nomi = nomi

    def boshlash(self):
        print("O‘yin boshlandi")

class Shaxmat(Oyin):
    def boshlash(self):
        print("Shaxmat boshlandi")

a = Shaxmat("Shaxmat")
a.boshlash()


# # 4
class Bino:
    def __init__(self, manzil):
        self.manzil = manzil

    def info(self):
        print("Bino mavjud")

class Maktab(Bino):
    def info(self):
        print("Bu maktab")

a1 = Bino("Toshkent")
a2 = Maktab("Samarqand")

a1.info()
a2.info()


# # 5
class Qush:
    def __init__(self, nomi):
        self.nomi = nomi

    def uchish(self):
        print("Uchmoqda")

class Kabutar(Qush):
    def uchish(self):
        print("Kabutar uchmoqda")

a = Kabutar("Kabutar")
a.uchish()
