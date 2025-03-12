### Point cloud distortion techniques

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

This venture leaves me with two questions:

1. How difficult is it to create more than three severities of noise?
2. How serious is it that the distortions are not consistent for different point clouds?
