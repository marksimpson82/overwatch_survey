def fix_typos(input_csv_path, output_csv_path):
    with open(input_csv_path) as f:
        text = f.read().replace("Brigette", "Brigitte")

    with open(output_csv_path, 'w') as f:
        f.write(text)
