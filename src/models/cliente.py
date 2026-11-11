class Cliente:
    def __init__(self, nome_cliente, email, pedidos):
        self.__nome_cliente = nome_cliente
        self.__email = email
        self.__pedidos = []
        self.atualizar_email(email)
        pass

    @property
    def nome_cliente(self):
        return self.__nome_cliente
    
    @property
    def email(self):
        return self.__email
    
    @property
    def pedidos(self):
        return self.__pedidos
    
    def atualizar_email(self, email):
        email = email.strip()
        if "@" not in email:
            raise ValueError("Email deve cconter @")
        else:
            self.__email = email

    def __str__(self):
        return f"self.__nome_cliente: {self.__nome_cliente}, email{self.__email}, pedidos {len(self.__pedidos)}"
        pass
    pass
        

