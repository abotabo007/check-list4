import re

def extract_c1_fields(dictionaries_path):
    with open(dictionaries_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Trova tutte le occorrenze ["nome", "nome_t", "nome_b", ...]
    pattern = r'\["(.*?)",\s*"(.*?)",\s*"(.*?)",'
    fields = re.findall(pattern, content)
    return set(field[0] for field in fields)


def extract_sql_fields(schema_path):
    with open(schema_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Isola solo la parte della tabella 'inspections'
    match = re.search(r'CREATE TABLE IF NOT EXISTS inspections\s*\((.*?)\)\s*;', content, re.S)
    if not match:
        raise ValueError("Tabella inspections non trovata nel file SQL")

    table_def = match.group(1)

    # Trova tutti i campi *_t o *_b
    field_names = set()
    for line in table_def.splitlines():
        line = line.strip().strip(',')
        if not line or line.startswith("FOREIGN KEY"):
            continue

        name = line.split()[0]
        if name.endswith("_t") or name.endswith("_b"):
            base = name.rsplit("_", 1)[0]
            field_names.add(base)
        else:
            field_names.add(name)

    # Rimuove i campi SQL standard
    std = {"i_id", "c_id", "u_id", "v_id", "miles", "next_oil", "next_1", "next_2", "date", "first_name", "last_name"}
    return field_names - std


def generate_sql_fields(missing_fields):
    lines = []
    for field in sorted(missing_fields):
        lines.append(f"{field} INTEGER, {field}_t TEXT, {field}_b BLOB")
    return lines


def generate_c1_lines(missing_fields):
    lines = []
    for field in sorted(missing_fields):
        label = field.replace("_", " ").capitalize()
        lines.append(f'["{field}", "{field}_t", "{field}_b", "{label}"]')
    return lines


def main():
    dictionaries_path = r"C:\Users\Dlia Abdessamad\Desktop\check-list3\fleets\dictionaries.py"
    schema_path = r"C:\Users\Dlia Abdessamad\Desktop\check-list3\fleets\schema.sql"

    c1_fields = extract_c1_fields(dictionaries_path)
    sql_fields = extract_sql_fields(schema_path)

    c1_not_in_sql = c1_fields - sql_fields
    sql_not_in_c1 = sql_fields - c1_fields

    print("\n--- 🛠️ Campi presenti in c1 ma NON nello schema.sql ---")
    for line in generate_sql_fields(c1_not_in_sql):
        print(line + ",")

    print("\n--- 🛠️ Campi presenti nello schema.sql ma NON in c1 ---")
    for line in generate_c1_lines(sql_not_in_c1):
        print("c1.append(" + line + ")")

    print("\n✅ Confronto completato.")


if __name__ == "__main__":
    main()
