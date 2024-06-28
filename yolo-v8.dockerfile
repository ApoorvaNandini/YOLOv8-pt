# Use NVIDIA CUDA base image
FROM nvcr.io/nvidia/pytorch:24.01-py3

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    rclone \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip3 install opencv-python==4.5.5.64
RUN pip3 install PyYAML
RUN pip3 install tqdm
RUN pip3 install pandas matplotlib Pillow pyquaternion shapely scikit-learn

#RUN rm -r /YOLOv8-pt/

# Copy local source code into the container
COPY ./ /YOLOv8-pt/

# Set working directory
WORKDIR /YOLOv8-pt

# Install additional Python dependencies
# RUN pip3 install -r requirements.txt

# Set entrypoint (if necessary)
# ENTRYPOINT ["python3", "your_script.py"]
