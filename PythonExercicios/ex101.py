def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 10:
        return f'Com idade {idade} anos: NÃO VOTA!'
    elif 16 <= idade <18 or idade > 65:
        return f'Com idade {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com idade {idade} anos: VOTO OBRIGATÓRIO!'


#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
