from typing import Union

account_numbers: str # номер счета
card_numbers: str # номер карты


def get_mask_card_number(card_numbers: Union[str]) -> str:
    """Функция, которая маскирует номер карты"""

    return f"{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[12:]}"


def get_mask_account(account_numbers: Union[str]) -> str:
    """Функция, которая маскирует счет"""

    return f"**{account_numbers[-4:]}"


print(get_mask_account("73654108430135874305"))

print(get_mask_card_number("7000792289606361"))
