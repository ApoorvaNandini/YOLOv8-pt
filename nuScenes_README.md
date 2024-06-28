## Step 1

* To download nuScenes Dataset go to https://www.nuscenes.org/ and sign-up/sign-in
* Download Full dataset (v1.0) Mini (3.88 GB) and extract the compressed folder for example at data root dir ~/yolov8/v1.0-mini

    ### Dataset structure

    ├── yolo-v8 
        ├── v1.0-mini
            ├── maps
                ├── abcde.png
                ├── cdefg.png
            ├── samples **
                ├── CAM_FRONT
                ├── CAM_FRONT_LEFT
                ├── CAM_FRONT_RIGHT
            ├── sweeps
                ├── CAM_FRONT
                ├── CAM_FRONT_LEFT
                ├── CAM_FRONT_RIGHT
            ├── v1.0-mini **
                ├── attribute.json
                ├── calibrated_sensor.json
                ├── category.json
                ├── ego_pose.json
                ├── image_annotations.csv
                ├── instance.json
                ├── log.json
                ├── map.json
                ├── sample_annotation.json
                ├── sample_data.json
                ├── sample.json
                ├── scene.json
                ├── sensor.json
                ├── visibility.json

* Convert 3d bbox labels to 2d bbox labels
    ```
    cd ~/yolo-v8/YOLOv8-pt/utils;python convert_annotations.py --dataroot=/home/asaridena/yolo-v8/v1.0-mini --version=v1.0-mini --image_limit=-1 --filename=image_annotations.csv
    ```
* Generate labels in YOLO-v8 format
    ```
    cd ~/yolo-v8/YOLOv8-pt/utils;python create_labels.py --dataroot=/home/asaridena/yolo-v8/v1.0-mini --version=v1.0-mini --annotations_filename image_annotations.csv --output_dir_name labels
    ```


