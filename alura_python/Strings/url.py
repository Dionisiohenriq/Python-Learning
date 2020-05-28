class url_tratativa:

    def __init__(self, url):
        if self.verifica_url(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        valores = self.encontra_valores()
        valores = valores.split(' ')
        return f'Moeda Origem: {valores[0]}\nMoeda Destino: {valores[1]}\nValor: {valores[2]}'

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def verifica_url(url):
        if url  and url.startswith('www.bytebank.com'):
            return True
        else:
            return False

    def encontra_valores(self):

        moeda_origem = 'moedaorigem='.lower()
        moeda_destino = 'moedadestino='.lower()
        valor = '$='

        valor_find_ind_init = self.query_moeda(valor)
        valor_find_ind_end = self.url.find('&')
        orig_find_ind_init = self.query_moeda(moeda_origem)
        orig_find_ind_end = self.url.find('&', 33)
        dest_find_ind_init = self.query_moeda(moeda_destino)

        moeda1 = self.url[orig_find_ind_init:orig_find_ind_end]
        moeda2 = self.url[dest_find_ind_init:]
        valor1 = self.url[valor_find_ind_init:valor_find_ind_end]

        if moeda1 == 'moedadestino':
           moeda1 = moeda1.replace('moedadestino', 'real', 1)

        texto = f'{moeda1} {moeda2} {valor1}'
        return texto

    def query_moeda(self, moeda):
        return self.url.find(moeda) + len(moeda)
