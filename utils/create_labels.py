import argparse
import convert_annotations
import csv
import os


def class_id_mapping(class_name):
    mapping = {
        'vehicle.car': 0,
        'vehicle.motorcycle': 1,
        'vehicle.bicycle': 2
    }
    return mapping.get(class_name, -1)

def extract_labels(csv_annotations_file_path, output_dir):
    with open(csv_annotations_file_path, newline='') as csvfile:
        header = csvfile.readline().strip().split(',')
        reader = csv.DictReader(csvfile, delimiter=',', fieldnames=header)
        next(reader)
        for row in reader:
            filename = row['filename'].split('/')[-1]
            class_id = class_id_mapping(row['category_name'])
            bbox_corners = eval(row['bbox_corners'])

            if class_id >= 0:
                output_filename = os.path.splitext(filename)[0] + '.txt'
                with open(os.path.join(output_dir, output_filename), 'a') as output_file:
                    output_file.write(f"{class_id} {bbox_corners[0]} {bbox_corners[1]} {bbox_corners[2]} {bbox_corners[3]}\n")
                    output_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image annotations into .txt label files for yolo-v8 combatibility.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataroot', type=str, default='/home/asaridena/yolo-v8/v1.0-trainval', help="Path where nuScenes is saved.")
    parser.add_argument('--version', type=str, default='v1.0-trainval', help='Dataset version.')
    parser.add_argument('--annotations_filename', type=str, default='image_annotations.csv', help='2d Annotations Output filename.')
    parser.add_argument('--output_dir_name', type=str, default='labels', help='Output directory.')
    args = parser.parse_args()

    csv_annotations_file_path = os.path.join(args.dataroot, args.version, args.annotations_filename)
    output_dir_name = os.path.join(args.dataroot, args.output_dir_name)
    extract_labels(csv_annotations_file_path, output_dir_name)