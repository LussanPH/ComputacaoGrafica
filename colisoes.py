import funcoes

def verificar_colisoes_gerais(hitboxes_djonga, lista_cachorros, lista_pombos):
    
    # 1. Condição: Iterar por cada parte do corpo do Djonga (Cabeça, Corpo)
    for hb_p in hitboxes_djonga:
        
        # 2. Condição: Checar contra cada cachorro na tela
        for cao in lista_cachorros:
            if "hitbox" in cao:
                # Se qualquer parte do player tocar no cachorro, houve colisão
                if funcoes.intersecao(*hb_p, *cao["hitbox"]):
                    return True
        
        # 3. Condição: Checar contra cada pombo na tela
        for ave in lista_pombos:
            if "hitbox" in ave:
                # Se qualquer parte do player tocar no pombo, houve colisão
                if funcoes.intersecao(*hb_p, *ave["hitbox"]):
                    return True
                    
    # Se percorreu tudo e não tocou em nada
    return False