from src.masks import get_mask_account, get_mask_card


def get_mask_result(string_with_info: str) -> str:
    """Возвращает исходную строку с замаскированным номером карты/счета"""
    division_string = string_with_info.split()
    if division_string[0] == "Счет":
        return f"{' '.join(division_string[:-1])} {get_mask_account(division_string[-1])}"
    return f"{' '.join(division_string[:-1])} {get_mask_card(division_string[-1])}"


def time_conversion(data_time: str) -> str:
    """Возвращает строку с датой в виде dd.mm.yy"""
    main_parts = data_time.split("-")[::-1]
    main_parts[0] = main_parts[0][:2]
    return ".".join(main_parts)


print(get_mask_result("Счет 64686473678894779589"))
