## Week 9 03-08 Mar

This week I am continuing work on the background chapter of my thesis. Right now, I am writing about PCQA techniques. The following is a summary of categories of NR PCQA techniques.

### Model-based NR PCQA techniques

NR PCQA techniques can roughly be divided into two categories: model-based and projection-based methods. Model-based techniques work by directly extracting information from the points inside the point cloud.

One influential model-based technique is ReSCNN, a convolutional approach to the problem of NR PCQA. ResSCNN consists of three parts: feature extraction, pooling and concatenation, scoring. In the feature extraction part, four groups of three sparse convolutional layers extract features from the points. Sparse convolutional layers are used as opposed to regular convolutional layers as the former works better with point clouds where many voxels are empty. The pooling and concatenation part downsamples the extracted features and combines the result into vectors of size 256 x 1. Lastly, ResSCNN has a scoring part consisting of two fully connected layers that outputs a final score. At the time of publication, ReSCNN outperformed all SOTA NR PCQA metrics and even some FR PCQA metrics.

Apart from using deep learning, some PCQA metrics take a page from IQA and use natural scene statistics (NSS). One such metric is 3D-NSS which uses NSS based on geometry and color information. It computes the 10-NN algorithm for all points in a point cloud, constructs a 3x3 covariance matrix and uses that to construct three eigen vectors. Those three eigen vectors are then used to compute curvature, anisotropy (a measure of how geometrical properties vary depending on direction), linearity, planarity, and sphericity. The color information is extracted by converting the colors from the RGB color space to the LAB color space. The geometry and color features are then used to compute a set of statistical properties including: mean, standard deviation, generalized Gaussian distribution (GGD), asymmetric GGD (AGGD), and the shape-rate Gamma distribution. The results of these are finally used by a support-vector regression to output the final scores.

### Projection-based NR PCQA techniques

Projection-based methods work by projecting the points in a point cloud onto a 2-dimensional plane. This is typically done using the V-PCC encoding which works by converting the point cloud to two video sequences, one with geometry information and one with textural information.

One of the first projection-based techniques were PQA-Net. PQA-Net has three modules: projection and feature extraction, distortion type classification, and quality prediction. In the first module, point clouds are projected onto six 2D image planes. Features are then extracted using a CNN with four convolutional blocks. The resulting feature vector is then used in classifying the type of the distortion. It also is fed to the quality prediction module which predicts the quality. The output of the distortion type classification module and the quality prediction module are then fused to produce a score.

A major issue in PCQA is the limited amount of training data which makes it difficult to create a robust metric. To overcome this issue, IT-PCQA applied domain adaption and transferred knowledge from IQA to PCQA. This is done using a conditional-discriminative network.

### Hybrid approaches

MM-PCQA is a hybrid approach that takes inspiration from both projection-based and model-based techniques. The main reason for combining the modalities is that you're able to cover a wider range of distortions than if you're only using one modality. MM-PCQA uses a symmetric cross-modality attention block to combine the two modalities. The results from doing this are very promising. The authors emphasize that this multi-modal technique outperformed all state-of-the-art NR PCQA techniques it was tested against. In a later article, the authors added better projection techniques and better encoders which resulted in even better results.
