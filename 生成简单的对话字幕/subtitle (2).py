import json


def split_character(text):
    character_cache = ''
    character_list = []
    is_special_character = 0

    for character_num in range(len(text)):
        character = text[character_num]

        if character_num + 1 > len(text):
            next_character = text[character_num + 1]

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


def subtitle_creater(subtitles: list, namespace: str, speed: int = 1):
    commands = {
        'init': [
            'scoreboard objectives add {} dummy'.format(namespace)
        ],
        namespace: []
    }

    # one screen
    for screen in subtitles:
        character_lists = []
        mean_num = 0

        for subtitle_num in range(len(screen)):
            character_list = split_character(screen[subtitle_num])
            mean_num += len(character_list)
            character_lists.append(character_list)

            #  if type(character) == list:
            #  character = ''.join(character)

        mean_num /= len(screen)
        play_data_dict = {}
        play_data_cache = {}

        #  {
            #  '0': {
                #  '0': 'H',
                #  '1': 'T',
                #  '2': 'T'
            #  }
        #  }

        # one line
        for character_list in character_lists:
            global_time = mean_num / len(character_list)
            play_data_dict[global_time] = {}

            # one character
            for character_num in range(len(character_list)):
                character = character_list[:character_num + 1]

                time = int(global_time * character_num * 100)

                # play_data_dict[-1][time] = character

            play_data_cache = play_data_dict

        __import__('ipdb').set_trace()
        #  for time, character in play_data_dict.items():
        #  commands[namespace].append('titleraw @a[scores={{{}={}}}] actionbar {{"rawtext":[{{"text":{}"}}]}}'.format(namespace, time, character))

    return commands


def main():
    subtitles = [[
        'Subtitle Creater programme.',
        'Made in China.'
    ]]

    result = json.dumps(subtitle_creater(subtitles, 'test', 1), sort_keys=True,
                        indent=4, separators=(', ', ': '), ensure_ascii=False)

    with open('test.json', 'w') as file:
        file.write(result)


if __name__ == '__main__':
    main()
