def get_words_count(content):
    return len(content.split())

def get_sorted_characters(characters):
    sorted = []
    
    def sort_on(items):
        return items["num"]

    for char in characters:
        if(char.isalpha()):
            entry = {"char": char, "num": characters[char]}
            sorted.append(entry)

    sorted.sort(reverse=True, key=sort_on)
    return sorted

def get_characters_count(content):
    characters = {}
    for character in content:
        if character.lower() in characters:
            characters[character.lower()] += 1
        else:
            characters[character.lower()] = 1

    return characters

