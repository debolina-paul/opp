class recensement:
    def __init__(self, l1, l2, l3):
        self.f2020 = l3
        self.f2019 = l2
        self.f2018 = l1

    def permanents (self):
        return [f for f in self.f2020 if
        f in self.f2019 and f in self.f2018]

#myversion(this works too)
# class listeelectorale(recensement):
    def __init__(self, l1, l2, l3):
        super().__init__(l1, l2, l3)


#Rafik
l = listeelectorale([jd, ad, cc],
                    [jd, ad, ma, cc], [ad, ma, cc])

for f in l.inscrits():
    print(f)

    