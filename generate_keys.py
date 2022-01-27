def get_all_partial_keys(plaintext_chars, ciphertext_chars):
    """
    :param plaintext_chars: list of most popular plaintext characters (in descending order)
    :param ciphertext_chars: list of most popular ciphertext characters (in descending order)
    :return: list of all partial keys (as dictionaries) from plaintext_chars into ciphertext_chars
    You may have more successful decryptions if the size of plaintext_chars is strictly less
    than the size of ciphertext_chars.
    """

    # Create global variable to store the partial keys generated
    # recursively by generate_all_partial_keys.
    global partial_key_list
    partial_key_list = list()

    # Must have at least as many ciphertext character options as
    # plaintext character options.
    if len(plaintext_chars) <= len(ciphertext_chars):
        generate_all_dictionaries(plaintext_chars, ciphertext_chars, dict())

    return partial_key_list


def generate_all_dictionaries(plaintext_chars, ciphertext_chars, partial_key):
    """
    Used by get_all_dictionaries to recursively generate all partial keys (as dictionaries)
    from plaintext_chars into ciphertext_chars.
    Dictionaries are stored in global variable partial_key_list and returned by get_all_dictionaries.
    Do not call generate_all_partial_keys directly. Instead call get_all_partial_keys.
    :param plaintext_chars: list of remaining plaintext characters
    :param ciphertext_chars: list of remaining ciphertext characters
    :param partial_key: list of partial key currently being generated
    :return: None
    """

    # Create global variable to store the partial keys generated
    # recursively by generate_all_partial_keys.
    global partial_key_list

    # If there are no plaintext characters remaining to be mapped,
    # append the current partial key to the global list.
    if len(plaintext_chars) == 0:
        partial_key_list.append(partial_key)

    # Otherwise, recursiely map the first plaintext character to
    # each possible ciphertext character
    else:
        for target_cipher_char in ciphertext_chars:

            # Create copies of all inputs to prepare the
            # recursive call.
            new_partial_key = partial_key.copy()
            new_plaintext_chars = plaintext_chars.copy()
            new_ciphertext_chars = ciphertext_chars.copy()

            # Map the first plaintext character to target_cipher_char and
            # remove both from future consideration.
            new_partial_key[plaintext_chars[0]] = target_cipher_char
            new_plaintext_chars.remove(plaintext_chars[0])
            new_ciphertext_chars.remove(target_cipher_char)

            # Recursively generate all partial keys containing the previous map
            generate_all_dictionaries(new_plaintext_chars, new_ciphertext_chars, new_partial_key)

# Example use case
partial_keys = get_all_partial_keys(['e', 't', 'a'], ['w', 'b', 't', 'x'])
print(partial_keys)
print(len(partial_keys))