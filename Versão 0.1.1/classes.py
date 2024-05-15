import random
"""
Classe Personagem
"""
class Inimigo():
    def __init__(self, nome,vida, danoMin, danoMax,posicaomapaX, posicaomapaY):
        self.nome = nome
        self.vida = vida
        self.danoMin = danoMin
        self.danoMax = danoMax
        self.posicaomapaX = posicaomapaX
        self.posicaomapaY = posicaomapaY
   
   
    """

    FUNÇÃO PARA RECEBER DANO

    """    
    def sofrerDano(self, dano):
        self.vida -= dano
        print("O personagem sofreu {dano} de dano, sua vida atual é: {self.vida}")

    def atacarPersonagem(self, personagem):
        dano = random.randint(self.danoMin, self.danoMax)
        personagem.sofrerDano(dano)
class Mapa():
    def __init__(self, larguraX, larguraY):
        self.larguraX = larguraX
        self.larguraY = larguraY        


"""
Classe Personagem
"""
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
        curaRealizada = random.randint(curaMin,curaMax)
        if(self.vida + curaRealizada > 10):
            self.vida = 10
            print("O personagem curou e está com a vida maxima")
        else:
            self.vida += curaRealizada     
            curaRealizada = str(curaRealizada)   
            print("O personagem se curou com "+curaRealizada)
    def sofrerDano(self, dano):
        self.vida -= dano
        dano = str(dano)
        print("O personagem sofreu "+dano+" de dano")

    """
    
    FUNÇÕES PARA ANDAR NO EIXO X E Y

    """

    def andarX(self, X):
        self.posicaoX += X
    def andarY(self, Y):
        self.posicaoY += Y    
    
    """

    FUNÇÕES PARA COMBATE

    """
    def combate(self, inimigo):
        print("Você entrou em combate com um inimigo")
        roundPersonagem = 1
        fugiu = False
        while(self.vida != 0 or fugiu is True):
            if(roundPersonagem == 1):
                print("Agora é sua vez! ")
                print("1. Atacar")
                print("2. Curar")
                print("3. Fugir")
                escolha = input("Escolha o que você irá fazer")
                if(escolha == 1):
                    self.atacarPersonagem(inimigo)
                elif(escolha == 2):
                    self.curar(1, 5)
                elif(escolha == 3):
                    fugiu = self.fugir()
                roundPersonagem = 2
            else: 
                print("Agora é a vez do inimigo")
                inimigo.atacarPersonagem(inimigo)
                roundPersonagem = 1


    def encontrarInimigo(self, posX, posY, posIX, posIY):
        if(posX == posIX and posY == posIY):
            print("Inimigo encontrado")
    def atacarPersonagem(self,inimigo):
        dano = random.randint(self.danoMin, self.danoMax)
        inimigo.sofrerDano(dano)
    def fugir():
        chance = random.randint(1,10)
        if(chance >= 5):
            print("A fuga foi realizada com sucesso")
            return True
        else:
            print("A fuga falhou! Continue a batalhar")
            return False    
