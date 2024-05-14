import ramdom
class Inimigo():
    def __init__(self, nome,vida, danoMin, danoMax,posicaoMapa):
        self.nome = nome
        self.vida = vida
        self.danoMin = danoMin
        self.danoMax = danoMax
        self.posicaoMapa = posicaoMapa
   
   
    """

    FUNÇÃO PARA RECEBER DANO

    """    
    def sofrerDano(self, dano):
        self.vida -= dano
        print("O personagem sofreu {dano} de dano, sua vida atual é: {self.vida}")

    def atacarPersonagem():
        dano = random.randint(self.danoMin, self.danoMax)
        Personagem.sofrerDano(dano)
class Mapa():
    def __init__(self, larguraX, larguraY):
        self.larguraX = larguraX
        self.larguraY = larguraY        


class Personagem():
    def __init__(self,nome,sexo):
        self.nome = nome
        self.sexo = sexo
        self.dano = 2
        self.vida = 10
        self.vigor = 10
        self.danoMin = 1
        self.danoMax = 5
        self.posicaoX = 0
        self.posicaoY = 0
        self.inventario = []
    
    """

    FUNÇÕES PARA ADIÇÃO E REMOÇÃO DE ITENS

    """
    
    def adicionarItem(self,item):
        self.inventario.append(item)
    
    def removerItem(self,item):
        self.inventario.append(item)    
    
    """
    
    FUNÇÕES PARA ADIÇÃO E REMOÇÃO DE VIDA NO PERSONAGEM

    """
    def curar(self, curaMin, curaMax):
        curaRealizada = ramdom.randInt(curaMin,curaMax)
        self.vida += curaRealizada
        print("O personagem se curou com {curaRealizada}")
    def sofrerDano(self, dano):
        self.vida -= dano
        print("O personagem sofreu {dano} de dano, sua vida atual é: {self.vida}")

    """
    
    FUNÇÕES PARA ANDAR NO EIXO X E Y

    """

    def andarX(self, X):
        self.posicaoX += X
    def andarY(self, Y):
        self.posicaoY += Y    
    
    """

    FUNÇÕES PARA ATACAR UM INIMIGO

    """

    def atacarPersonagem():
        dano = random.randint(self.danoMin, self.danoMax)
        Inimigo.sofrerDano(dano)
