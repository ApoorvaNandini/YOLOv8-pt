import argparse
import pandas as pd
import random
from sklearn.model_selection import train_test_split


def train_and_test_split(data_root,original_annotations_file, train_output_file, test_output_file, test_size=0.1):
    df = pd.read_csv(data_root + original_annotations_file)

    df = df[['filename', 'map_name']]
    print(len(df))
    df.drop_duplicates(inplace=True)
    print(len(df))
    df.to_csv(data_root + "no_dups_" + original_annotations_file, index=False)
    
    # Split the dataset into train and test sets
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=42)

    # Write the train and test sets to CSV files
    #train_df.to_csv(data_root + "no_dups_" + train_output_file, index=False)
    #test_df.to_csv(data_root + "no_dups_" + test_output_file, index=False)


def split_dataset(
    data_root: str,
    superset_annotations_file: str,
    original_annotations_file: str,
    original_dataset_fraction: float,
    output_file_name: str
):
    original_df = pd.read_csv(data_root + "no_dups_" + original_annotations_file)
    super_df = pd.read_csv(data_root + "no_dups_" + superset_annotations_file)

    rows_to_select = int(len(original_df) * original_dataset_fraction)

    selected_rows = random.sample(range(len(super_df)), rows_to_select)

    df_selected = super_df.iloc[selected_rows]
    #df_selected.to_csv(data_root + "no_dups_" + output_file_name, index=False)


if __name__ == '__main__':

    dataset_name = "v1.0-mini"

    train_and_test_split('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston.csv', 'image_annotations_boston_train_p9.csv', 'image_annotations_boston_val_p1.csv', 0.1)

    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p9.csv', 'image_annotations_boston.csv', 0.8, 'image_annotations_boston_train_p8.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p8.csv', 'image_annotations_boston.csv', 0.7, 'image_annotations_boston_train_p7.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p7.csv', 'image_annotations_boston.csv', 0.6, 'image_annotations_boston_train_p6.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p6.csv', 'image_annotations_boston.csv', 0.5, 'image_annotations_boston_train_p5.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p5.csv', 'image_annotations_boston.csv', 0.4, 'image_annotations_boston_train_p4.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p4.csv', 'image_annotations_boston.csv', 0.3, 'image_annotations_boston_train_p3.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p3.csv', 'image_annotations_boston.csv', 0.2, 'image_annotations_boston_train_p2.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_boston_train_p2.csv', 'image_annotations_boston.csv', 0.1, 'image_annotations_boston_train_p1.csv')

    train_and_test_split('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore.csv', 'image_annotations_singapore_train_p9.csv', 'image_annotations_singapore_val_p1.csv', 0.1)

    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p9.csv', 'image_annotations_singapore.csv', 0.8, 'image_annotations_singapore_train_p8.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p8.csv', 'image_annotations_singapore.csv', 0.7, 'image_annotations_singapore_train_p7.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p7.csv', 'image_annotations_singapore.csv', 0.6, 'image_annotations_singapore_train_p6.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p6.csv', 'image_annotations_singapore.csv', 0.5, 'image_annotations_singapore_train_p5.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p5.csv', 'image_annotations_singapore.csv', 0.4, 'image_annotations_singapore_train_p4.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p4.csv', 'image_annotations_singapore.csv', 0.3, 'image_annotations_singapore_train_p3.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p3.csv', 'image_annotations_singapore.csv', 0.2, 'image_annotations_singapore_train_p2.csv')
    split_dataset('/home/asaridena/yolo-v8/'+dataset_name+'/'+dataset_name+'/', 'image_annotations_singapore_train_p2.csv', 'image_annotations_singapore.csv', 0.1, 'image_annotations_singapore_train_p1.csv')


