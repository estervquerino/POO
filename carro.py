class Carro:
    def __init__(self, modelo, ano, cor, limite_velocidade):
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor
        self.combustível = 0 
        self.ligado = False
        self.velocidade = 0 
        self.limite_velocidade = 200

    def ligar(self):
        if self.combustível > 0:
            self.ligado = True
            print(f"{self.modelo} ligou!")
        else:
            print(f"{self.modelo} está sem combustível, abasteça!")

    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print(f"{self.modelo} foi desligado!")
        else:
            print(f"{self.modelo} está em movimento, não pode ser desligado!")

    def acelerar(self):
        if self.ligado is True:
            if self.combustível >=5:
                if self.velocidade <= self.limite_velocidade:
                    self.velocidade += 10
                    self.combustível -= 5
                    print(f"{self.modelo} está a {self.velocidade} km/h.")
                else:
                    print(f"{self.modelo} está no limite de velocidade!")
            else:
                print(f"{self.modelo} está sem combustível!")
        else:
            print(f"{self.modelo} está desligado!")

    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"{self.modelo} freou, {self.velocidade} km/h")
        else:
            print(f"{self.modelo} está parado!")

    def abastecer(self, quantidade):
        if self.combustível + quantidade < 100:
            self.combustível += quantidade
            print(f"{self.modelo} foi abastecido, combustível: {self.combustível}")
        else:
            print(f"Abastecimento acima do limite do combust´vel")
        
    def buzinar(self):
        print(f"{self.modelo}: BEEP BEEP!")

    def status(Self):
        print(f"Modelo: {self.modelo}")
        print(f"Combustível: {self.combustível}")
        print(f"cor: {self.cor}")
        print(f"Velocidade atual: {self.velocidade} km/h")
        print(f"Ano: {self.ano}")
        print(f"Ligado: {self.ligado}")
        print(f"Limite de velocidade: {self.limite_velocidade} km")

carro1 = Carro("Chevette o verdinho", 1990, "Verde Escuro", 151)
carro1.ligar()
carro1.abastecer(80)
carro1.acelerar(100)
carro1.abastecer(80)
carro1.buzinar()
carro1.status()
carro1.acelerar(100)
carro1.frear()
carro1.desligar()
for i in range(10):
    carro1.acelerar(10)
carro1.desligar


        
