import tablestats


def main():
    filename = input().strip()
    try:
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return
    rows = tablestats.read_rows(lines)
    counts = tablestats.count_types(rows)
    print(len(rows))
    print(len(counts))
    print(tablestats.total_minutes(rows, "ошибка"))
    summary = tablestats.to_csv(counts)

    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(summary)

if __name__ == "__main__":
    main()