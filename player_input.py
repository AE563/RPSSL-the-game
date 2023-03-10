from announce import dictionary_fighter


def player_choice():
    while True:
        list_check = [1, 2, 3, 4, 5]
        input_data = int(input('Enter the number:'))
        if input_data in list_check:
            return dictionary_fighter[input_data]
        else:
            print('You entered the wrong number. Try enter 1')
