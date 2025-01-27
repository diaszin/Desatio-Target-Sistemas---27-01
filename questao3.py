import json


def media_faturamento_diario(faturamento_diário: list[dict[str]]):
    soma = 0
    quantidade = 0
    
    for faturamento in faturamento_diário:
        valor = faturamento["valor"]
        
        if valor > 0:
            soma += valor
            quantidade += 1
            
    
    return soma/quantidade
        
    
        
    

arquivo = open("./dados.json", "r", encoding="utf-8")

faturamento = json.loads(arquivo.read())

menor_valor = None
maior_valor = None
dias_faturamento_maior_que_media_mensal = []

media = media_faturamento_diario(faturamento)

for registro in faturamento:
    valor = registro["valor"]
    dia = registro["dia"]
    
    if valor > 0 and (menor_valor is None or menor_valor["valor"] > valor):
        menor_valor = {
            "dia": dia,
            "valor": valor
        }
    if valor > 0 and (maior_valor is None or maior_valor["valor"] < valor):
        maior_valor = {
            "dia": dia,
            "valor": valor
        }
        
    if valor > media:
        dias_faturamento_maior_que_media_mensal.append(dia)



print(f"""
O menor valor ocorreu no dia {menor_valor["dia"]} com o valor de: {menor_valor["valor"]}      
O maior valor ocorreu no dia {maior_valor["dia"]} com o valor de: {maior_valor["valor"]}
Os dias que o faturamento foi maior que a média mensal, foram os: 
""")

for dia in dias_faturamento_maior_que_media_mensal:
    print(f"Dia: {dia}")
