def soma(a, b):
    if isinstance(a, str) or isinstance(b,str):
        return "Erro: Não é permitido strings"
    elif isinstance(a, 
        (int,float)) and isinstance(b,(int,float)):
        return a + b

def subtracao(a, b):
    if isinstance(a, str) or isinstance(b,str):
        return "Erro: Não é permitido strings"
    elif isinstance(a, 
        (int,float)) and isinstance(b,(int,float)):
        return a - b

def multiplicacao(a, b):
    return a * b
