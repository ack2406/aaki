
def check_aby(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if token_prev.text == "tak":
        result["insert"] = True
        result["insert_pos"] = -1
    if token.pos_ == 'CCONJ':
        pass
    elif token.pos_ == 'PART' or token.pos_ == 'SCONJ':
        result["insert"] = True

    
    return result


def check_czy(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if token.pos_ == 'CCONJ':
        pass
    elif token.pos_ == 'PART' and token_prev.pos_ != 'CCONJ' and token_prev.pos_ != 'PART':
        result["insert"] = True
    elif occured:
        result["insert"] = True
    return result


def check_lub(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if occured:
        result["insert"] = True
    elif token.pos_ == 'CCONJ':
        pass

    result['occured'] = True

    return result


def check_oraz(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if occured:
        result["insert"] = True
    elif token.pos_ == 'CCONJ':
        pass

    result['occured'] = True
    return result

# podrzedne zdania dodac
def check_jak(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_że(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if token_prev.pos_ == 'CCONJ':
        pass
    elif token_prev.pos_ == 'PART' or (token_prev.pos_ == 'ADV' and token_prev.dep_ == 'mark'):
        # if previous token is at the beginning of the sentence
        if token_prev.i != 0:
            result["insert"] = True
            result["insert_pos"] = -1
    else:
        result["insert"] = True
    return result


def check_a(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if token.pos_ == 'CCONJ' and token_prev.pos_ != 'PART':
        pass
    elif token.pos_ == 'PART' and token_prev.pos_ != 'CCONJ' and token_prev.pos_ != 'PART':
        result["insert"] = True
    return result

# podrzedne zdania
def check_niż(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_ale(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    if token.pos_ == 'NOUN':
        result["insert"] = False

    return result

#kontekst (dopowiedzenie)
def check_albo(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if occured:
        result["insert"] = True

    return result


def check_lecz(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result


def check_ponieważ(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result


def check_więc(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    if token.pos_ == 'PART':
        result["insert_pos"] = False
    elif token_prev.text == 'a':
        result["insert_pos"] = -1
    
    return result

#wtrącenia
def check_czyli(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

#współdzilene zdania
# spójnik wynikowy
def check_i(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if occured:
        result["insert"] = True
    return result


def check_bądź(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result

#odmiany która/którego/itd.
def check_który(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    if token_prev.text == 'w' or token_prev.text == 'a':
        result["insert_pos"] = -1

    return result


def check_bo(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

#nie kumam
def check_ani(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    if occured:
        result["insert"] = True
    return result


def check_żeby(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

#zdanie podrzędne + pełne wyrażenia
def check_gdy(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    return result

#współrzędne/pojedynce
def check_natomiast(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

#wtrącenia
def check_zanim(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

#kontekst wyrażenia
def check_zatem(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    return result

#wtrącenia
def check_gdzie(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    if token_prev.text == 'tam':
        result["insert_pos"] = -1

    return result

#wtraćenia
def check_kiedy(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

#wtrącenia
def check_by(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result


def check_aż(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    if token.pos_ == 'PART':
        result["insert"] = False

    return result


def check_to(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_jednak(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    

    return result


def check_iż(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    result["insert"] = True

    return result


def check_gdyż(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    result["insert"] = True

    return result


def check_także(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_tylko(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_nawet(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_chociaż(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_jakby(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_skoro(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_bowiem(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_stąd(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_dopóki(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_choć(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_dlatego(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_co(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_w(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_wraz(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result

def check_jako(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result

def check_jeśli(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result

def check_jeżeli(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result
