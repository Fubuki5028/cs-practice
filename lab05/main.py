import tablestats

filename = input().strip()
with open(filename, encoding="utf-8") as f:
    lines = f.readlines()
rows = tablestats.read_rows(lines)
counts = tablestats.count_types(rows)
print(len(rows))
print(len(counts))
print(tablestats.total_minutes(rows, "ошибка"))
summary = tablestats.to_csv(counts)
with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(summary)
