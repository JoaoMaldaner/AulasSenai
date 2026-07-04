def desenhar_caixa(largura):
    print("+" + "-" * largura + "+")
    
    for i in range(3):
        print("|" + " " * largura + "|")
    
    print("+" + "-" * largura + "+")

desenhar_caixa(18)


