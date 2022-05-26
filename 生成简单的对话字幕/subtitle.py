def split_character(text):
    character_cache = ''
    character_list = []
    is_special_character = 0

    for character_num in range(len(text)):
        character = text[character_num]

        if character_num + 1 > len(text):
            next_character = text[character_num + 1]

        del character_num

        if is_special_character == 0:
            if character == '§' and next_character != '§' or character in ['\\', ' ']:
                character_cache += character

                if character == '§' and next_character != '§' or character == '\\':
                    is_special_character = 1
                elif character == '§' and next_character != '§':
                    is_special_character = 2
            else:
                character_list.append(''.join([character_cache, character]))
                character_cache = ''
        elif is_special_character == 1:
            character_cache += character
            is_special_character = 0
        else:
            is_special_character = 0

    return character_list


def subtitle_creater(subtitles: list, namespace:str, speed: int=1):
    commands = {
        'init': [
            'scoreboard objectives add {} dummy'.format(namespace)
        ],
        namespace: []
    }

    for screen in subtitles:
        play_data = []
        character_lists = []

        mean_num = 0

        for subtitle_num in screen:
            character_lists.append(split_character(screen[subtitle_num]))
            mean_num += len(character_lists)

        mean_num /= len(screen)

        for character_list in character_lists:
            play_data_list.append([])

            for character_list_num in len(range(character_list)):
                character_list = character_lists[character_list_num]
                character = character_list[0, character_list_num]
                del character_list_num

                if type(character) == list:
                    character = ''.join(character)

                play_data_list[-1].append([mean_num / len(character_list), character])

            for play_data in play_data_list:
                # commands[namespace].append('title @a[scores={{{}={}}}] actionbar {}'.format(namespace, mean_num / len(character_list) * speed * 20, character))
                pass

    return commands


def main():
    subtitles = [[
        'Hello, world!',
        'This is only a test!'
    ]]

    subtitle_creater(subtitles, 'test', 1)


if __name__ == '__main__':
    main()

