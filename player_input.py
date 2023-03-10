from announce import dictionary_fighter


def player_choice():
    input_data = int(input('Enter the number:'))
    return dictionary_fighter[input_data]
