dictionary_fighter = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors',
    4: 'Spock',
    5: 'Lizard'
}


def player_choice():
    print('(ง •̀_•́)ง')
    for k, v in dictionary_fighter.items():
        print(k, ':', v)
    input_data = int(input('Choose your fighter, enter the number:'))
    return dictionary_fighter[input_data]
