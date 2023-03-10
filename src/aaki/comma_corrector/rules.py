
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
    result = {"insert": False, "insert_pos": 0, "occured": True}
    if token.pos_ == 'CCONJ':
        pass
    elif token.pos_ == 'PART' and token_prev.pos_ != 'CCONJ' and token_prev.pos_ != 'PART':
        result["insert"] = True
    elif occured:
        result["insert"] = True
    return result


def check_lub(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": True}
    if occured:
        result["insert"] = True
    elif token.pos_ == 'CCONJ':
        pass

    result['occured'] = True

    return result


def check_oraz(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": True}
    if occured:
        result["insert"] = True
    elif token.pos_ == 'CCONJ':
        pass

    result['occured'] = True
    return result

# podrzedne zdania dodac
def check_jak(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    # zaimek wprowadzający zdanie/wypowiedzenie podrzędne
    # wyrażenie wprowadzające porównanie o charakterze dopowiedzenia
    # wprowadza ono wyliczenie lub wyszczególnienie
    # zarówno, jak; równie, jak; tak, jak i; tak, jak

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
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    if token.pos_ == 'CCONJ' and token_prev.pos_ != 'PART':
        result["insert"] = False
    elif token.pos_ == 'PART' and token_prev.pos_ != 'CCONJ' and token_prev.pos_ != 'PART':
        result["insert"] = True
    return result

# podrzedne zdania
def check_niż(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    # spójnik wprowadza zdanie podrzędne
    # spójnik wprowadza równoważnik zdania
    # Nie stawiamy: spójnik występuje przed członem porównawczym w zdaniu pojedynczym

    return result


def check_ale(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}
    if token.pos_ == 'NOUN':
        result["insert"] = False

    return result

#kontekst (dopowiedzenie)
def check_albo(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": True}
    if occured:
        result["insert"] = True

    return result

# zrobione
def check_lecz(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

def check_ponieważ(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    # zasada dotycząca stawiania przecinka po zdaniu składowym, gdy ponieważ stoi na początku na początku zdania złożonego

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
def i_test(sentence):
    comma_list = [False]
    tmp = sentence.split(" i ")
    if len(tmp) > 2:
        for t in range(len(tmp)):
            if t == 0:
                comma_list.append(False)
            else:
                if "," in tmp[t-1]:
                    comma_list.append(False)
                else:
                    comma_list.append(True)
    else:
        return sentence
    result = tmp[0] 
    for i in range(1,  len(tmp)): 
        if comma_list[i-1]:
            result += ', i '
        else:
            result += ' i '
        result += tmp[i]
    return result

# do zredagowania
def check_bądź(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": True}

    # jeżeli occured to wstaw przecinek
    if occured:
        result["insert"] = True

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
    result = {"insert": False, "insert_pos": 0, "occured": True}
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

    # spójnik - chyba git - sprawdza, czy jest jednym z dwóch rodzajów spójnika
    if token.pos_ == 'CCONJ' or token.pos_ == 'SCONJ':
        result["insert"] = True

    return result


def check_jednak(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}
    
    # spójnik
    if token.pos_ == 'CCONJ' or token.pos_ == 'SCONJ':
        result["insert"] = True
    # nie stawiamy przed partykułą
    if token.pos_ == 'PART':
        result["insert"] = False

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

    # przed "a także"
    if token_prev.text == 'a':
        result["insert_pos"] = -1
        result["insert"] = True

    return result


def check_tylko(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    # dla partykuły "tylko" nie wstawiamy przecinka
    if token.pos_ == "PART":
        result["insert"] = False

    return result

# XD powodzenia
def check_nawet(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_chociaż(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    # spójnik
    if token.pos_ == 'CCONJ' or token.pos_ == 'SCONJ':
        result["insert"] = True
    # nie stawiamy przed partykułą
    if token.pos_ == 'PART':
        result["insert"] = False

    return result

# zdania składowe, podrzędne i takie tam
def check_jakby(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


def check_skoro(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    # dodatkowe zasady dla:
    ## pisane na początku zdania
    ## pisane w środku zdania

    return result

# zdanie pojedyncze
def check_bowiem(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    # dodatkowe zasady dla:
    ## przecinek przed całym wprowadzeniem
    ## jeśli zdanie pojedyncze to brak przecinka

    return result


def check_stąd(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    # spójnik
    if token.pos_ == 'CCONJ' or token.pos_ == 'SCONJ':
        result["insert"] = True


    return result


def check_dopóki(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    # dodatkowe zasady dla:
    ## jeśli na początku zdania
    ## jako składniki połączeń dopóki...,dopóty...; dopóki...,póty...; dopóty...,dopóki...

    return result


def check_choć(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    # spójnik
    if token.pos_ == 'CCONJ' or token.pos_ == 'SCONJ':
        result["insert"] = True
    # nie stawiamy przed partykułą
    if token.pos_ == 'PART':
        result["insert"] = False

    return result


def check_dlatego(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result


def check_co(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    # co jest przed orzeczeniem
    if token_prev.pos_ == 'VERB':
        result["insert"] = True

    # dodać zasady dla:
    ## wprowadza zdanie składowe

    return result

# Zdania składowe złożone, wystepuje razem z zaimkiem
def check_w(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result


# zasadniczo nie stawia się przed nim przecinka, chyba że wprowadza wtrącenie
def check_wraz(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}


    return result

# zasadniczo nie stawia się przed nim przecinka, chyba że wprowadza wtrącenie lub określa przyczynę
def check_jako(token, token_prev, occured=False):
    result = {"insert": False, "insert_pos": 0, "occured": occured}

    return result

# jeśli wystepuje na początku zdania złożonego, oddzielamy przecinkiem zdanie składowe
def check_jeśli(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

# jeśli wystepuje na początku zdania złożonego, oddzielamy przecinkiem zdanie składowe
def check_jeżeli(token, token_prev, occured=False):
    result = {"insert": True, "insert_pos": 0, "occured": occured}

    return result

def complex_sentence(doc, sentence):
    commas = []
    for token in doc:
        shift = 0
        s_tree = list(token.subtree)
        if s_tree[0].text == "i":
            continue
        if len(s_tree) > 1 and token.dep_ != "ROOT" and token.pos_ in ["AUX", "VERB"]:
            if s_tree[0] == doc[0]:
                while(s_tree[-1].text != sentence[token.i + shift]):
                    shift += 1
                shift += 1
            else:
                while(s_tree[0].text != sentence[token.i + shift]):
                    shift -= 1
            commas.append(token.i + shift)
    return sorted(commas)
