# ChromSTEM-Denoising-Autoencoder

## Objective
Utilize a denoising autoencoder with convolutional neural networks and molecular dynamics simulations to enhance the resolution of ChromSTEM images, achieving nucleosome-level clarity.

## Introduction
Scanning transmission electron microscopy tomography, when complemented with ChromEM staining, is termed as ChromSTEM. This powerful method unveils the 3D intricacies of genome organization. However, a clear interpretation of these images can be marred by noise. Our solution to this challenge is a uniquely designed denoising autoencoder (DAE).

## About the DAE
The DAE is powered by convolutional neural networks and enriched with insights from molecular dynamics simulations. Its training regimen is based on synthetic images, precisely those originating from the 1-cylinder per nucleosome (1CPN) chromatin model. Such a foundation enables our autoencoder to proficiently filter out noise and simultaneously capture the deep-rooted structural details inherent in ChromSTEM experiments.

## Key Features
- **Improved Denoising Capability**: Outperforms a wide range of denoising algorithms.
- **Structural Integrity**: Retains and highlights the subtle structural features of ChromSTEM images.
- **Tetranucleosome Resolution**: Demonstrates adeptness in resolving intricate tetranucleosome motifs.
- **High-Resolution Imaging**: Unravels minute domains within larger chromatin-dense territories and brings individual nucleosomes into sharp focus.

### Requirements
- Python 3.x
- TensorFlow v2.9.1 (or higher)
- Keras
- NumPy
- Matplotlib
- h5py
- glob
- idx2numpy
- Pillow (PIL)
- OpenCV (cv2)
- SciPy
- timeit
- Scikit-learn

### Contributing
If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcomed.

### License
This project is licensed under the MIT License. See `LICENSE.md` for details.

### Feedback
Any feedback or suggestions are greatly appreciated!




