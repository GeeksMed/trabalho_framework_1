class class_produto:
    def __init__(self, id=int, nome_produto=str, descricao=str, valor=float, quantidade=int):
        self.__id = id
        self.__nome_produto = nome_produto
        self.__descricao = descricao
        self.__valor = valor
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome_produto(self):
        return self.__nome_produto

    @nome_produto.setter
    def nome_produto(self, nome_produto):
        self.__nome_produto = nome_produto

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
