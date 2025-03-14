class Cachorro:
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.energia =- 100 
        self.acordado = True
        self.feliz = True
        
    
    def comer(self, quantidade):
        if self.acordado:
         self.comida -= quantidade
         self.feliz = True
         print(f"O cachorro {self.nome} está comendo {quantidade} unidades de comida")
        else:
           print(f"O cachorro {self.nome} está dormindo e não pode comer")

    def acordar(self):
       self.acordado = True
       print(f"está acordado")


    def dormir(self):
        self.energia = 100
        self.acordado = False
        print(f"dormindo")
        
    def brincar(self):
        if self.acordado:
            if self.energia >=20:
                self.energia -= 20
                self.feliz = True
                self.acordado = True
                print(f"O cachorro {self.nome} está brincando")
            else:
               print(f"{self.nome} está sem energia")
        else:
           print(f"O cachorro {self.nome} está dormindo e não pode brincar")

    def latir(self):
        if self.acordado:
           print(f"latindo")
        else:
            print(f"dormindo")

meu_cachorro = Cachorro("tobby", 6, "pastor alemão", 10)
meu_cachorro.comer(5)
meu_cachorro.dormir()
meu_cachorro.acordar()
meu_cachorro.latir()
meu_cachorro.dormir()
meu_cachorro.acordar()
meu_cachorro.brincar()
meu_cachorro.brincar()
meu_cachorro.brincar()
meu_cachorro.brincar()
meu_cachorro.brincar()
meu_cachorro.brincar()
meu_cachorro.dormir()
meu_cachorro.acordar()
meu_cachorro.brincar()