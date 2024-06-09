def hide_card(card_number):
    res = 12 * "*" + card_number.replace(" ", "")[12:]
    return res

print(hide_card("905 678123 45612 56"))