def vowel_consonant_char(ch):
    match ch:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return "Vowel"
        case _:
            return "Consonant"

