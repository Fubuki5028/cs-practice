def read_rows(lines):
    header = None
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = [field.strip() for field in line.split(',')]
        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue
        row_dict = dict(zip(header, fields))
        rows.append(row_dict)
    return rows

if __name__ == "__main__":
    print(read_rows(["2026-03-01,запуск,1.5", "2026-03-01,ошибка,0.4"]))
