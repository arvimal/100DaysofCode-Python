NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    NAMES_NEW = []
    for name in NAMES:
        if name.title() not in NAMES_NEW:
            NAMES_NEW.append(name.title())
        else:
            pass
    return NAMES_NEW


def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    names = sorted(names, key=lambda a: a.split()[-1], reverse=True)
    return names


def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    return sorted(names)[0].split()[0]
