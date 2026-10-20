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

def count_types(rows):
    counts = {}
    for row in rows:
        t= row.get('тип')
        if t:
            counts[t] = counts.get(t, 0) + 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row.get('тип') == kind:
            mins_str = row.get('минуты', '')
            if not mins_str:
                continue
            try:
                val = float(mins_str.replace(',', '.'))
                total += val
            except ValueError:
                pass
    return round(total, 1)


if __name__ == "__main__":
    print(read_rows(["2026-03-01,запуск,1.5", "2026-03-01,ошибка,0.4"]))
