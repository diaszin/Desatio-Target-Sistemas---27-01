def total_mensal(faturamento: dict):
    soma = 0
    for estado in faturamento.keys():
        valor =faturamento[estado]
        
        soma += valor
    
    return soma


def calcula_porcentagem(parte, total):
    porcentagem = (parte/total) * 100
    
    return porcentagem

def calcular_porcentagem_por_estado(faturamento: dict):
    total = total_mensal(faturamento)
    for estado in faturamento.keys():
        valor =faturamento[estado]
        porcentagem = calcula_porcentagem(valor, total)
        
        print(f"{estado} representa {porcentagem}% de {total}")
        
    


faturamento_mensal ={
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53
}


calcular_porcentagem_por_estado(faturamento_mensal)