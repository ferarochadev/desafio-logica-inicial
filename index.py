
heroi = str(input('Digite o nome do herói: '))


while True:
    
    xp = int(input('Digite a quantidade de xp do herói: '))
     
    if xp < 1000:
        nivel = 'Ferro'
        break
    elif 1000 <= xp < 2000:
        nivel = 'Bronze'
        break
    elif 2000 <= xp < 5000:
        nivel = 'Prata'
        break
    elif 5000 <= xp < 6000:
        nivel = 'Ouro'
        break
    elif 6000 <= xp < 7000:
        nivel = 'Platina'
        break
    elif 7000 <= xp < 8000:
        nivel = 'Ascendente'
        break
    elif 8000 <= xp < 9000:
        nivel = 'Imortal'
        break
    else:
        nivel = 'Radiante'
        break
        
print(f'O herói de nome {heroi} está no nível de {nivel}.')

