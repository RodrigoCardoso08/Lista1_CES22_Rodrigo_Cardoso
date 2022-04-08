"""Crie exemplos que ilustrem as diferenças e as vantagens entre métodos abstratos, métodos estáticos,
métodos de classe e métodos de instância."""
import abc


class Lanche(object):
    def __init__(self, comprimento, largura, altura):
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura

    @staticmethod
    def area_base(comprimento, largura):
        return comprimento * largura

    @classmethod
    def volume(cls, altura, comprimento, largura):
        return altura * cls.area_base(comprimento, largura)

    @abc.abstractmethod
    def pegar_medidas(self):
        """Return medidas do objeto lanche"""

    def get_volume(self):
        return self.volume(self.altura, self.comprimento, self.largura)


"""Aqui temos que area_base é um método estático. É importante ressaltar que area_base não depende do estado
do objeto em si e que é possível sobrescrever esse método em uma subclasse. O método estático só pode utilizar
os próprios parâmetros em suas alterações."""

"""Volume é um método de classe. Esse tipo de método permite que utilizemos os métodos da classe em que
está inserido sem que seja necessário utilizarmos um objeto dessa classe."""

"""Pegar_medidas é um método abstrato. Isso quer dizer que qualquer classe que tenha como herança a classe
Lanche terá que ter definido dentro de si um método próprio chamado pegar_medidas."""

"""Por fim, volume é um método de instância. Ele pode utilizar variáveis provindos de outras instâncias e suas
variáveis podem ser utilizadas por outras instâncias."""