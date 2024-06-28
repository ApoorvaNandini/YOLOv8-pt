import csv

def filter_csv(input_file, output_file, keyword):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            if keyword.lower() in row['map_name'].lower():
                writer.writerow(row)

# Input and output file paths
input_file = '/home/asaridena/yolo-v8/v1.0-mini/v1.0-mini/image_annotations.csv'
output_file = '/home/asaridena/yolo-v8/v1.0-mini/v1.0-mini/image_annotations_boston.csv'

# Keyword to filter for
keyword = 'boston'

# Filtering the CSV file
filter_csv(input_file, output_file, keyword)


