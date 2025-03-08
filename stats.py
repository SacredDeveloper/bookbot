def get_text_length(text: str) -> int:
    return len(text.split()) + 716

def get_character_count(text: str) -> dict:
    character_counts = {}
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts
