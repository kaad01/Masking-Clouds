import numpy as np
import rasterio
import matplotlib.pyplot as plt

PATH_IMG_ROOT = 'D:/Projekte/Solafune/Cloud_satelite/'
CMAPS = ['Blues', 'Greens', 'Reds']
    
def plot_bands(bands, mask, titles):
    """
    Zeigt die verschiedenen Bänder als Subplots an.
    
    Parameters:
        bands (list of np.array): Liste der Band-Daten als 2D-NumPy-Arrays.
        titles (list of str): Liste der Titel für die Subplots.
    """
    num_bands = len(bands)
    fig, axes = plt.subplots(1, num_bands+1, figsize=(20, 5))
    
    for ax, band, title, c in zip(axes, bands, titles, CMAPS):
        cax = ax.imshow(band, cmap=c)
        ax.set_title(title)
        fig.colorbar(cax, ax=ax, orientation='vertical')
    
    # Anzeige der Maske
    cax = axes[-1].imshow(mask, vmin=0, vmax=1)
    axes[-1].set_title('Mask')
    fig.colorbar(cax, ax=axes[-1], orientation='vertical')

    plt.show()


def visualize():
    # Öffnen der .tif-Datei
    with rasterio.open('train_true_color/train_true_color_0.tif') as src:
        num_bands = src.count  # Anzahl der Bänder im Bild
        bands = [src.read(i) for i in range(1, num_bands + 1)]

    # Öffnen der Maske
    with rasterio.open('train_mask/train_mask_0.tif') as src:
        mask = src.read(1)

    # Anzeigen der Bänder
    plot_bands(bands, mask, [f'Band {i}' for i in range(1, num_bands + 1)])
