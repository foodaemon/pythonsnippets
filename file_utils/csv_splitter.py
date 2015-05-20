import os
import csv


def split(file_handler, delimiter=",", quotechar=None, row_limit=500000, output_path='.', keep_headers=True):
    with open(file_handler, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar='"')
        current_piece = 1
        current_out_path = os.path.join(output_path, "output_%s.csv" % current_piece)
        current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
        current_limit = row_limit
        if keep_headers:
            headers = next(reader, None)
            current_out_writer.writerow(headers)
        for i, row in enumerate(reader):
            if i + 1 > current_limit:
                current_piece += 1
                current_limit = row_limit * current_piece
                current_out_path = os.path.join(output_path, "output_%s.csv" % current_piece)
                current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter, quotechar=quotechar)
                if keep_headers:
                    current_out_writer.writerow(headers)
            current_out_writer.writerow(row)

if __name__ == '__main__':
    split('./file_name.csv', quotechar='"', row_limit=2)
