LINE_TEMPLATE = '{sep} {num:<{num_width}} {sep} {name:^{name_width}} {sep} {price:>{price_width}} {sep}'

NAME_COL_IDX = 0
PRICE_COL_IDX = 1

NUM_SUFFIX = '.'
PRICE_SUFFIX = ' Ft'
DEFAULT_SEPARATOR = '#'


def get_max_col_len(table, col_idx):
    max_col_len = None
    for row in table:
        col = row[col_idx]
        col_len = len(str(col))
        if max_col_len is None or col_len > max_col_len:
            max_col_len = col_len
    return max_col_len


def get_num_width(veggies):
    num_of_digits = len(str(len(veggies)))
    return num_of_digits + len(NUM_SUFFIX)


def get_name_width(veggies):
    return get_max_col_len(veggies, NAME_COL_IDX)


def get_price_width(veggies):
    return get_max_col_len(veggies, PRICE_COL_IDX) + len(PRICE_SUFFIX)


def get_widths(veggies):
    return {
        'num': get_num_width(veggies),
        'name': get_name_width(veggies),
        'price': get_price_width(veggies),
    }


def get_line(i, veggie, widths):
    num = '{}{}'.format(i + 1, NUM_SUFFIX)
    name = veggie[0]
    price = '{}{}'.format(veggie[1], PRICE_SUFFIX)
    return LINE_TEMPLATE.format(**{
        'sep': DEFAULT_SEPARATOR,
        'num': num,
        'name': name,
        'price': price,
        'num_width': widths['num'],
        'name_width': widths['name'],
        'price_width': widths['price'],
    })


def get_lines(veggies):
    widths = get_widths(veggies)
    lines = []
    for i, veggie in enumerate(veggies):
        lines.append(get_line(i, veggie, widths))
    return lines


def add_top_and_bottom_line(lines):
    line_width = len(lines[0])
    sep_line = DEFAULT_SEPARATOR * line_width
    lines.insert(0, sep_line)
    lines.append(sep_line)


def print_veggies(veggies):
    lines = get_lines(veggies)
    add_top_and_bottom_line(lines)
    for line in lines:
        print(line)


def main():
    print_veggies([
        ['alma', 100],
        ['répa', 40],
        ['vöröshagyma', 210],
        ['káposzta', 300],
        ['sárgabarack', 232132],
        ['szőlő', 500],
        ['paprika', 20],
        ['karalábé', 710],
        ['őszibarack', 42],
        ['szilva', 10],
        ['jégsaláta', 1420],
    ])

if __name__ == '__main__':
    main()
