class MinhaClasse: 
    # metodos especiais
    def __enter__(self):
        print("Entreiiiii")


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("sai")

with MinhaClasse() as mc:
    print("Executando codigo dentro do with")