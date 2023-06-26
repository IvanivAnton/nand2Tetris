class SymbolTable:
    def __init__(self) -> None:
        self.__table__ = {}

    def add(self, symbol, address):
        self.__table__.update({symbol: address})

    def contains(self, symbol):
        return symbol in self.__table__.keys()

    def get(self, symbol):
        return self.__table__[symbol]