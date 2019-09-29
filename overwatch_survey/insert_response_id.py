import csv


def insert_response_id(input_csv_path, output_csv_path):
    """
    Inserts a unique response_id into every record -- just doing this so we can use it as a foreign key later
    """
    r = csv.reader(open(input_csv_path))
    lines = list(r)

    response_id = 0
    lines[0].insert(0, "Response_id")

    for line in lines[1:]:
        line.insert(0, response_id)
        response_id += 1

    w = csv.writer(open(output_csv_path, 'w'), lineterminator='\n')
    w.writerows(lines)
