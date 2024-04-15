from src.masks import get_mask_account, get_mask_card


def get_mask_result(string_with_info: str) -> str:
    """ Возвращает исходную строку с замаскированным номером карты/счета"""
    if len(string_with_info.split()) > 2:
        return get_mask_card(string_with_info)
    else:
        return get_mask_account(string_with_info)


def time_conversion(data_time: str) -> str:
    """ Возвращает строку с датой в виде dd.mm.yy"""
    main_parts = data_time.split("-")[::-1]
    main_parts[0] = main_parts[0][:2]
    return ".".join(main_parts)
