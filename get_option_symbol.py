COLUMNS = 12


def main():
    data = read_all()
    data = select_option(data)
    data = select_nk225(data)
    data = select_first_month(data)
    output_result(data)


def read_all():
    data = []
    with open("option_list.csv") as f:
        for line in f:
            line = line.strip()
            columns = line.split(",")
            if len(columns) != COLUMNS:
                continue
            data.append(columns)
    return data


def select_option(data: list[str]) -> list[str]:
    result = []
    for row in data:
        if row[2] == "CAL" or row[2] == "PUT":
            result.append(row)
    return result


def select_nk225(data: list[str]) -> list[str]:
    result = []
    for row in data:
        if row[11] == "日経225":
            result.append(row)
    return result


def select_first_month(data: list[str]) -> list[str]:
    fm = data[0][3]
    result = []
    for row in data:
        if row[3] == fm:
            result.append(row)
    return result


def output_result(data: list[str]):
    with open("symbol.txt", "w") as f:
        for row in data:
            print(row[0], file=f)


if __name__ == "__main__":
    main()
