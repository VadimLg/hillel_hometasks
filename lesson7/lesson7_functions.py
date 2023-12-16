def list_sorting_increase_int(list_in: list) -> list:
    return sorted(list_in)


def list_sorting_descending_int(list_in: list) -> list:
    return sorted(list_in, reverse=True)

def list_sorting_increase_str_lenght(list_in: list) -> list:
    return sorted(list_in, key=len)
