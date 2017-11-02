class Vozilo:

    def __init__(self, dolzina, teza, barva,):
        self.dolzina = dolzina   #ko bomo nardili na novo en objekt vozilo, neko dejansko vozilo, mu bo priredil
        self.teza = teza                           #ta inicializacijski parameter
        self.barva = barva



    def uporabi_trobljo(self):
        return 'beep'

class Avto(Vozilo):

    def __init__(self, dolzina, teza, barva, tip_motorja, koda):
        Vozilo.__init__(self, dolzina, teza, barva)
        self.tip_motorja = tip_motorja
        self.koda = koda
        self.odklenjen = False

    def odkleni_zakleni(self, koda, odkleni=True):
        if koda == self.koda and odkleni:
            self.odklenjen = True

            return 'Zmig, Zmig'
        elif koda == self.koda and not odkleni:

            self.odklenjen = False
            return 'Zmig, zmig, zmig, zmig'
        else:
            raise Exception('Run before I kill you!')

if __name__ == '__main__':                   #ta if preverja ali je to kar je zagnano res ta fajl, nek z importanjem
    moj_avto = Avto(4.2, 1200, 'modra', 'TDI', 'krneki')

    print(moj_avto.odkleni_zakleni('krneki'))
    print(moj_avto.odkleni_zakleni('krneki', odkleni=False))
    print(moj_avto.barva)
    print(moj_avto.teza)
    print(moj_avto.dolzina)
    print(moj_avto.tip_motorja)
    print(moj_avto.uporabi_trobljo())



    moje_kolo = Vozilo(1.9, 7, 'rumen')

    print(moje_kolo.barva)
    print(moje_kolo.teza)
    print(moje_kolo.dolzina)
    print(moje_kolo.uporabi_trobljo())