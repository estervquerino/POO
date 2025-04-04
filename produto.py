class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.quantidade = quantidade
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Não é permitido valor negativo")

produto1 = Produto("Prego", 1.5, 200)
