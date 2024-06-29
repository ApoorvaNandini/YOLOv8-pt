import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_mAP(exp_dir, results_file, total_epochs=500):

    # Load data from CSV
    results_file_path = os.path.join(exp_dir, results_file)
    data = pd.read_csv(results_file_path)

    # Extracting columns
    epochs = data['epoch']
    val_map = data['val mAP']
    train_map = data['train mAP']

    # Plotting
    plt.plot(epochs, val_map, label='Validation mAP')
    plt.plot(epochs, train_map, label='Train mAP')

    # Adding labels and title
    plt.xlabel('Epoch')
    plt.ylabel('mAP')
    plt.title('Train and Validation mAP over Epochs')

    # Set x-axis range
    plt.xlim(0, total_epochs)

    # Adding legend
    plt.legend()

    # Display the plot
    plt.grid(True)

    # Check if plot file already exists, delete it if it does
    plot_file = exp_dir + 'mAP_plot.png'
    if os.path.exists(plot_file):
        os.remove(plot_file)

    plt.savefig(plot_file)
    plt.close()