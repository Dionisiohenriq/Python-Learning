# herança é usada tanto para o reuso, quanto para absorver o polimorfismo(ducktyping),
# herança pelo polimorfismo - atributos, métodos
# herança pelo reuso de código e remoção de duplicação
# herança = extensão
# composição = conceito de 'tem um' ao invés de 'é um'
# Classes abstract based classes - abc - obrigam a implementar métodos da superclasse nas classes
# filhas
# herança múltipla, utiliza os métodos na ordem classe > superclasse > superclasse em mesmo nível hierárquico, super-superclasse
# classes mixin são utilizadas para criar comportamentos(métodos) que são utilizados em classes complexas

class Playlist():

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def tamanho(self):
        return len(self._programas)

    @property
    def listagem(self):
        return  self._programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    # def __iter__(self):
    #     return self._programas.__iter__()

    def __str__(self):
       return [print(programas) for programas in self._programas]