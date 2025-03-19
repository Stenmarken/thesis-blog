### Point cloud distortion techniques

This article has a bunch of math formulas that won't render on the blog. Use [this](https://github.com/Stenmarken/thesis-blog/blob/main/Ideas/pc_distortions/pc_distortions.md) link instead.

The problem with many PC distortion techniques is that they're tailored to one or a few datasets. [MultiCorrupt](https://github.com/ika-rwth-aachen/MultiCorrupt), which we had plans of using is tailored only to the nuScenes dataset. I've gone through the code briefly and I have no idea how I would modify to work with our dataset.

[Robo3D](https://github.com/ldkong1205/Robo3D) isn't tailored to one specific dataset but works with any dataset that has the same format as KITTI, Waymo, or nuScenes. Using Robo3D, I started off by copying the `kitti_c` folder to a new folder called `roadview_c`. To get anything running I first had to change the `fog.sh` bash script that generates the corrupted files. In the `fog.sh`, you specify the source directory, the destination directory, and `beta` which is the backscatter coefficient. In Robo3D, there are 3 values of `beta` to choose from: `[0.008, 0.05, 0.2]`. The higher the coefficient, the more severe the fog. It's only possible to have three severities since they use lookup tables of integrals for those values. If you wanted other values, then you would have to precompute integrals for those values.

Having changed the `fog.sh` script, I then made some necessary changes to the `fog_simulation.py`. The main thing I had to change here was making sure that the script read the correct files.

Finally, I created three versions of the `fog.sh` script with the three different scatter values and ran the scripts.

Having created the distorted point clouds, I visualized them in Rerun. To do this, I had to make some assumptions about the data in the point clouds. I assumed that each point was stored as `(x, y, z, intensity)` and therefore did the following transformation when reading a point cloud file.

```python
return np.fromfile(path, dtype="<f4").reshape(-1, 4)
```

Then when I send the points to Rerun, I only included the first three channels as Rerun only wants `(x, y, z)` coordinates.

The distortions seem to work rather well. The fog distortions cause points to appear right in front of the vehicle that aren't there for the undistorted point cloud. It's also clear that a larger `beta` value results in more points appearing. Below you can see four images of point clous: one that is undistorted, one with light fog (`beta = 0.008`), one with moderate fog (`beta = 0.05`), and one with heavy fog (`beta = 0.2`).

| ![images/undistorted.png](images/undistorted.png) |
| :-----------------------------------------------: |
|                    Undistorted                    |

| ![images/light.png](images/light.png) |
| :-----------------------------------: |
|               Light fog               |

| ![images/moderate.png](images/moderate.png) |
| :-----------------------------------------: |
|                Moderate fog                 |

| ![images/heavy.png](images/heavy.png) |
| :-----------------------------------: |
|               Heavy fog               |

There are also some issues with the fog particles changing rapidly over time. During some timestamps, the `light` fog looks very similar to the `undistorted` point cloud (see the picture of the `light` fog) only for it in the next timestamp to have a bunch of fog particles in front of the vehicle. It's possible to see this in action at this [link](https://drive.google.com/drive/u/0/folders/1hgRfwG5Oup-RjSe7DjTPg4_NTosy7ItI).

This process leaves me with two questions:

1. How difficult is it to create more than three severities of noise?
2. How serious is it that the distortions are not consistent for different point clouds?

### Understanding how Robo3D works

Understanding the inner workings of Robo3D is necessary if I want to distort point clouds with more severity levels than the three previously mentioned. I'll limit the scope to looking only at fog for now.

One thing that's unclear is that the authors specify that the authors specify that the formula for calculating a fog point is the following.

$$
\begin{equation}
\hat{\mathbf{p}} = C_{\text{fog}}(\mathbf{p}) = \begin{cases}
(\hat{p}^{x}, \hat{p}^{y}, \hat{p}^{z}, p^{i_{\text{soft}}}), & \text{if } p^{i}_{\text{soft}} > p^{i_{\text{hard}}}, \\
(p^{x}, p^{y}, p^{z}, p^{i_{\text{hard}}}), & \text{else}.
\end{cases}
\quad
\end{equation}
$$

Under clear weather, a hard target is a solid object which has an attenuation coefficient of `0`. Under foggy weather, the hard target still exists but an additional soft target is added which provides distributed scattering. Calculating the intensity of a hard target under foggy weather is done with the formula:

$$
\begin{equation}
p^{i_{\text{hard}}} = p^i e^{-2\alpha \sqrt{(p^x)^2 + (p^y)^2 + (p^z)^2}}
\quad
\end{equation}
$$

where $\alpha$ is the attenuation coefficient. Basically, under fog, the intensity of the reflected light of hard objects will decrease as the fog attenuates the signal.

The soft target has the followig formula

$$
\begin{equation}
p^{i}_{\text{soft}} = p^{i} \frac{(p^{x})^{2} + (p^{y})^{2} + (p^{z})^{2}}{\beta_{0}} - \beta \times p^{i_{\text{tmp}}} \quad (1)
\end{equation}
$$

where $\alpha$ is the attenuation coefficient, $\beta$ is the backscatter coefficient, and
$p^{i_{\text{tmp}}}$ is the received response for the soft target term. $p^{i_{\text{tmp}}}$ is precomputed using a script in the GitHub repository.

The way equation 1 works is that it calculates the intensity for the soft target, i.e. the fog, and for the hard target which is the actual point in the point cloud. Then if the resulting instensity is greater for the soft target, then it replaces the hard target point in the point cloud with the fog point.

There are three important configuration variables here: attenuation coefficient ($\alpha$), backscattering coefficient ($\beta$), and the differential reflectivity ($\beta_0$). Attenuation is the effect of the light scattering or being absorbed by the fog/rain particles in the air. A higher $\alpha$ means that more light is being absorbed/scattered. The way Robo3D implements it is that the attenuation coefficient is uniformly sampled from `[0, 0.005, 0.01, 0.02, 0.03, 0.06]`. I have to make sure that when I am distorting the point clouds, that I have the same $\alpha$ for the same point cloud at different distortion levels. Backscattering is when fog particles/rain particles cause the signal to reflect meaning that we register a "false" point in the point cloud. $\beta$ is a coefficient for how much backscattering occurs. Differential reflectivity is a measure of the variation of reflectivity based on factors like wavelength, polarization, and the angle of incidence. This is perhaps also something I have to consider in my calculations. The standard in the code is just to have it set to $3.1830988618379064e-07$.

CANNOT HAVE IT SO THAT ALPHA IS VARYING RANDOMLY. EVEN WITH SEEDING THE RANDOMNESS WILL CAUSE PROBLEMS BECAUSE RIGHT NOW IT READS THE FILES IN A NON-DETERMINISTIC ORDER.

#### Increasing the number of distortions

Increasing the number of distortions means pre-computing the integrals for additional $\beta$ values. Why more heavy fog means a higher backscatter value but not necessarily a higher attenuation value is a question I don't know the answer to. Why not increase both the attenuation and the backscattering for more heavy fog?

Generating the precomputed integrals requires first the alpha values to include. I will not specify these and instead just use the default ones `[0.0, 0.005, 0.01, 0.02, 0.03, 0.06]`. Then I added it so you specify the beta value. Next I have to consider the `r_0_max` which is the maximum range. I had it use the default value of $200$. Next I have to specify the number of steps `n_steps`. I had it use the default again which is `arguments.n_steps = 10 * arguments.r_0_max`. It's possible to incorporate shift but I have no idea what does and it's turned off by default. Lastly, I specify the `save_path`.

In `generate_integral_lookup_table.py`, it has this statement:
`from theory import ParameterSet, P_R_fog_soft`. `theory` is not a module in the project so I changed it to `from fog_simulation import ParameterSet, P_R_fog_soft` as it is in `fog_simulation` that those methods can be found.

One weird thing is that in `fog_simulation.py`, `simulate_fog` is called with `noise` being set to `10` which is then used in `P_R_fog_soft`. This is done without any explanation. However, in `generate_integral_lookup_table.py`, it lacks a parameter for the `noise` when calling `P_R_fog_soft`, so I set that parameter to 10.

Nevermind, the problem is bigger. Calling the `P_R_fog_soft` from `generate_integral_lookup_table.py` requires a bunch of extra info. This might be difficult.
