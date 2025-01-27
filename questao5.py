def inverter_string(frase: str):
    nova_frase = ""
    
    for ind_letra in range(1, len(frase)+1):
        nova_frase += frase[-1*ind_letra]
        
    return nova_frase

frase = "moana busca casa de prego"
frase_invertida = inverter_string(frase)

print(frase_invertida)