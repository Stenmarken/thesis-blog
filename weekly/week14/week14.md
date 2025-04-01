## Week 14 - 31 Mar - 5 Apr

### Preliminary results from NR-PCQA

I've spent this week and last week trying out methods of NR-PCQA on distorted point clouds. As I elaborated on in [this](../../Ideas/pc_distortions/pc_distortions.md) blogpost, I could distort point clouds using different attenutation coefficients which corresponded to different severities.

I distorted a set of 295 point clouds from the `000` sequence in the `rehearse` dataset. I used alpha values of `[0.005, 0.01, 0.02, 0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21]` which meant that each point cloud had 10 distorted copies.

I used two NR-PCQA techniques for evaluation: MM-PCQA and MS-PCQE. MM-PCQA is a hybrid between projection-based and model-based NR-PCQA and was very simple to use. The MM-PCQA repository has a file called `test_single_ply.py` which I modified to take an input directory of PLY files, a model path, and an output path of where the scores should end up. The only thing I had to consider when using this method was the choice of model. For simplicity's sake, I chose the `WPC.pth` model as it was the standard choice. Perhaps, I could get better performance if I chose a model trained on a different dataset. One problem with MM-PCQA that I hadn't anticipated was that the program for some point clouds completely crashed. I have to figure out why this is the case at some point. For now, I simply removed those point clouds entirely (note that if `000184_alpha_0.05.ply` broke, then I removed all of the distorted copies `000184.ply`). This meant that I was left with 252 lists of 10 point clouds with various distortions.

I first ran all of the point clouds through MM-PCQA to get a score. Then, I aggregated the scores so I had a dictionary that looked like this:
```
{
    0.ply: [alpha_0.005_score, alpha_0.01_score, alpha_0.02_score, ...]
    1.ply: [alpha_0.005_score, alpha_0.01_score, alpha_0.02_score, ...]
}
```
Then for each element in the dictionary, I calcuated the Spearman Rank Correlation Coefficient(SROCC) by passing in the value of the list and the list of the filenames (0-19). This resulted in the following results:

```
sroccs[:20]: [-0.01, 0.12, 0.89, 0.75, 0.38,
              0.65, 0.71, 0.19, -0.35, 0.16,
              0.56, 0.52, -0.1, 0.5, 0.47,
              0.68, 0.83, -0.08, 0.73, 0.84]
Mean of sroccs: 0.53
Standard deviation of sroccs: 0.31
```

Note here that the mean and the standard deviation here are for the total 252 point clouds. It isn't totally clear exactly what these results mean. Having a mean of 0.53 indicates that there is overall a positive correlation but I have to combine the p-values of the SROCCs to be able to determine if it's a statistically significant result.

Running MS-PCQE was far more complicated than running MM-PCQA. Since, it's a projection-based method, it projects point clouds onto the image plane. So each point cloud is projected onto the image plane 6 times using various rotations and this process is repeated twice for different zoom values (0.4 and 0.6). Exactly what to set the zoom values to isn't clear. I'll ask the authors about this on their GitHub.

Finally, when this pre-processing is finished, I could try and figure out how to actually run the scoring bit of MS-PCQE. This mainly meant changing things in the `test.py` file like changing the input parameters and saving the results to a file. One choice I have to consider carefully here is the model to use in the evaluation. By model I mean the pytorch model to use in the score evaluation. For this experiment, I used a model trained on the `LSPCQA` dataset. Also, I only ran this experiment using 20 point clouds with 10 different severities. The reason for this is that transferring the files from the Dopamine server to my home computer took quite some time and I wanted to finish this experiment in a reasonable amount of time.

Running all of the point clouds and plotting the results gave out this:

```
SROCCs: [ 0.31,  0.81,  0.12,  0.66,  0.56,  0.18,  0.81,  0.49,  0.85,
        0.18,  0.14, -0.15, -0.59,  0.61, -0.15,  0.09,  0.48,  0.73,
        0.81,  0.54, -0.15]
Standard deviation: 0.39
Mean: 0.35
```

Again, we see a a positively correlated result generally with a mean of 0.39. Although, there is a lot of variation considering that the standard deviation is 0.35. Furthermore, an interesting thing is that the scores are very similar for very different severity types. The following shows the scores for the point clouds 0-20. In each list, we start with `alpha=0.005`, then `alpha=0.01`, then `alpha=0.02`, `alpha=0.03`, `alpha=0.06`, `alpha=0.09`, `alpha=0.12`, `alpha=0.15`, `alpha=0.18`, and `alpha=0.21`. Looking at the score for 1.ply, it has a good SROCC value of 0.81 but still the differences between the values are very small. Surely, we would expect greater differences in scores than this.

```
scores for 0.ply: [1.35, 1.32, 1.33, 1.32, 1.31, 1.29, 1.35, 1.33, 1.33, 1.51]
scores for 1.ply: [1.29, 1.33, 1.32, 1.33, 1.37, 2.2, 1.35, 1.43, 1.41, 1.61]
scores for 2.ply: [1.33, 1.81, 1.34, 2.11, 1.41, 1.34, 1.37, 1.38, 1.39, 1.37]
scores for 3.ply: [1.34, 1.33, 1.37, 1.39, 1.37, 1.35, 1.58, 1.37, 1.4, 1.38]
scores for 4.ply: [1.33, 1.35, 1.36, 1.33, 1.35, 1.49, 1.34, 1.93, 1.36, 1.39]
scores for 5.ply: [1.71, 1.29, 1.33, 1.33, 1.42, 1.42, 1.41, 1.37, 1.5, 1.38]
scores for 6.ply: [1.34, 1.32, 1.41, 1.33, 1.4, 1.41, 1.4, 1.41, 2.19, 1.43]
scores for 7.ply: [1.33, 1.37, 1.41, 1.95, 1.51, 1.6, 1.51, 1.5, 1.47, 1.54]
scores for 8.ply: [1.29, 1.31, 1.39, 1.42, 1.45, 1.73, 1.45, 1.46, 1.88, 1.46]
scores for 9.ply: [1.4, 1.33, 1.37, 1.34, 1.38, 1.35, 1.37, 1.36, 1.35, 1.41]
scores for 10.ply: [1.31, 1.53, 1.46, 1.32, 1.33, 1.35, 1.34, 1.33, 1.38, 1.39]
scores for 11.ply: [1.32, 1.78, 1.64, 1.33, 1.43, 1.41, 1.42, 1.4, 1.4, 1.41]
scores for 12.ply: [1.31, 1.53, 1.32, 1.33, 1.3, 1.31, 1.3, 1.31, 1.3, 1.31]
scores for 13.ply: [1.33, 1.31, 1.36, 1.62, 1.41, 1.38, 1.37, 1.37, 1.42, 1.56]
scores for 14.ply: [1.84, 1.32, 1.6, 1.28, 1.35, 1.71, 1.35, 1.81, 1.34, 1.32]
scores for 15.ply: [2.2, 1.35, 1.37, 1.34, 2.04, 1.35, 1.72, 1.44, 1.4, 1.42]
scores for 16.ply: [1.34, 1.34, 1.95, 1.4, 1.36, 1.98, 1.37, 1.87, 1.44, 1.65]
scores for 17.ply: [1.35, 1.31, 1.36, 1.36, 1.51, 1.37, 1.43, 1.4, 1.44, 1.42]
scores for 18.ply: [1.31, 1.31, 1.33, 1.31, 1.34, 1.36, 1.76, 1.36, 1.48, 1.35]
scores for 19.ply: [1.3, 1.37, 1.37, 1.35, 1.39, 1.38, 1.4, 1.5, 1.36, 1.38]
scores for 20.ply: [1.3, 1.59, 1.82, 1.77, 1.37, 1.33, 1.37, 1.34, 1.36, 1.41]
```
