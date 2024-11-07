from typing import Union
from src.masks import get_mask_card_number, get_mask_account

number_account_card: str # номер вводимого счета или карты
user_data: str # дата и время пользователя

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


def get_date(user_data: Union[str]) -> str:
    """Функция, которая изменяет формат даты"""
    data_day = user_data.split("Т")[0]

    return f"{(user_data[8:10])}.{(data_day.split('-')[-2])}.{(data_day.split('-')[-3])}"




print(mask_account_card("Visa Platinum 8990922113665229"))
print(get_date("2024-03-11T02:26:18.671407"))


