from typing import Union
from src.masks import get_mask_card_number, get_mask_account
number_account_card: str # номер вводимого счета или карты

def mask_account_card(number_account_card: Union[str]) -> str:
    """ Функция, которая маскирует номер счета или карты"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for i in number_account_card:
        if i.isalpha():
            text_result += i
        elif i.isdigit():
            digit_result += i
            digit_count += 1
    if digit_count > 16:
        return f"{text_result} {get_mask_account(digit_result)}"
    else:
        return f"{text_result} {get_mask_card_number(digit_result)}"


print(mask_account_card("Visa Platinum 8990922113665229"))
