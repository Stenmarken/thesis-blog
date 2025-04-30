## Running MM-PCQA and MS-PCQE with simulated colors

### Simulated colors

Both MM-PCQA and MS-PCQE expect point clouds with points of the form P = (x,y,z,r,g,b) where (x,y,z) consist of the coordinate information and (r,g,b) consist of the color information.

As the point clouds used in the thesis do not contain (r,g,b) information, and instead only contains intensity values. I will have to simulate the appearance of color using the values of (r=i, g=i, b=i).

Let's perform the necessary preprocessing for one point cloud in order to understand how this works. What I first had to do was to re-scale the intensities after the fog distortion had executed. I had missed this part of the paper but it's a necessary step. This was done in the Robo3D repository.

### Running MS-PCQE

Next, in the `rotation.py` file of MS-PCQE, there were a few changes I had to make. Firstly, I changed the input from PLY files to the distorted KITTI-styled bin files instead. Then I ran the following lines to get the point cloud with intensity determining the RGB color info:

```
kitti_pc = np.fromfile(path, dtype=np.float32).reshape(-1, 4)
xyz = kitti[:, :3]
intensities = kitti_pc[:, 3]

intensity_normalized = intensities / 255.0
colors = np.stack([intensity_normalized, intensity_normalized, intensity_normalized], axis = 1)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utilityVector3dVector(xyz)
pcd.colors = o3d.utilityVector3dVector(colors)
```

Each of the point clouds is projected onto an image twice using two different zooms. First a zoom of 0.4 and a zoom of 0.6.

The `test.py` file seems to assume that the images have the names 0000.ply, 0001.ply, ...

I have no idea why this is but we'll just have to deal with it. I created a file `rename_dirs.py` that renames the directories according to the following mapping:

```
mapping = {
        "0.01.bin": "000000.ply",
        "0.02.bin": "000001.ply",
        "0.03.bin": "000002.ply",
        "0.04.bin": "000003.ply",
        "0.05.bin": "000004.ply",
        "0.06.bin": "000005.ply",
        "0.07.bin": "000006.ply",
        "0.08.bin": "000007.ply",
        "0.09.bin": "000008.ply",
        "0.1.bin": "000009.ply",
    }
```

Now I have to make sure that I'm calculating the SRCC and the KRCC in the correct ways. For MS-PCQE, higher scores mean better scores. The authors don't mention this explicitly in the paper but it's discernible if you look at Figure 1 in the MS-PCQE paper. In the set of point clouds used in the execution, the least distorted point clouds appear first and the most distorted point clouds go last. This means that I want the scores to decrease as I increase the distortion. In other words, I want a **negative** correlation close to -1.

For further use: if you want to use any other than 10 point clouds, then make sure to change the `database/rehearse_data_info/0-20.csv` file because that's the file currently used. When you run `test.py` now it expects that there are 10 point clouds in each directory. It's also the names here that are expected for the directories containing the projected images.


