def p_decorate(func):
    def func_wrapper(*arguments, **keywords):
        print("Texto de saída que nao esta presente em pegar_elementos_dialogo")
        return "<p>{0}</p>".format(func(*arguments, **keywords))

    return func_wrapper


class Dialogo(object):
    def __init__(self):
        self.nome = 'Rodrigo'
        self.sobrenome = 'Cardoso'

    @p_decorate
    def pegar_elementos_dialogo(self):
        return self.nome+""+self.sobrenome


meu_dialogo = Dialogo()

print(meu_dialogo.pegar_elementos_dialogo())
