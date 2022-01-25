def get_all_dictionaries(domain, codomain):
    """
    Set domain to be the most frequent plaintext characters (in descending order).
    Set comain to be the most frequent ciphertext characters (in descending order).
    You may have more successful decryptions if the size of domain is strictly less than the size of codomain.
    :param domain: domain of map as a list
    :param codomain: codomain of map as a list, must be at least as large as domain
    :return: list of all injective maps (as dictionaries) from domain into codomain
    """

    global dictionary_list
    dictionary_list = list()

    if len(domain) <= len(codomain):
        generate_all_dictionaries(domain, codomain, dict())

    return dictionary_list


def generate_all_dictionaries(domain, codomain, partial_map):
    """
    Used by get_all_dictionaries to recursively generate all injective maps (as dictionaries) from domain
    into codomain. Dictionaries are stored in global variable dictionary_list and returned by get_all_dictionaries.
    :param domain: domain of map as a list
    :param codomain: codomain of map as a list, must be at least as large as domain
    :param partial_map: partial injection that is built recursively
    :return: None
    """


    global dictionary_list

    if len(domain) == 0:
        dictionary_list.append(partial_map)
    else:
        for target_elt in codomain:
            new_partial_map = partial_map.copy()
            new_domain = domain.copy()
            new_codomain = codomain.copy()

            new_partial_map[domain[0]] = target_elt
            new_domain.remove(domain[0])
            new_codomain.remove(target_elt)

            generate_all_dictionaries(new_domain, new_codomain, new_partial_map)

print(get_all_dictionaries(['a', 'b'],['x','y','z']))
