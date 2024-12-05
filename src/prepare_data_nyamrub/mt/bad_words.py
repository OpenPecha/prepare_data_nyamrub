from better_profanity import profanity

def has_bad_words(text:str):
    if profanity.contains_profanity(text):
        return True
    return False 