### Week 3 - 20-24 January

#### Libraries for image distortions
Last week I tinkered with the `imagecorruptions` library in python to create distorted images. 
It's quite a nice library since it can add noise that occur in images taken by 
AV sensors. It can add motion, defocus, and zoom blurs as well as add 
noise simulating snow, frost, brightness, and fog. This is all well 
and good but the problem with the library is that it can only add 
5 levels of noise to an image. This means that for any given noise, 
you can only get back 5 images with different levels of that noise. 
Ideally you'd want to be able to take an image and a noise type and 
generate 100 images with various amounts of that noise type. Thus, 
I decided to look at some alternatives to `imagecorruptions` and see 
if those offered this feature. Here are some alternatives:

#### Wand
Wand is a python-binding for ImageMagick, a tool for editing 
and manipulating digital images. It has many features for distorting 
images but they consist mainly of mathematical functions. It's possible 
to do affine transformations, scalings, rotations, translations, and rezizings. 
However, it's not possible to directly add things like motion blur or snow noise. 
It's much more low-level than this.

I guess that it's an option to implement various blurs/distortions 
myself using Wand but it would most likely take some time. 
I would also have to get in the weeds of understanding how all of the distortions 
work (and cover things like images of different sizes). Ultimately, I'm not super 
excited about that and I won't get into it unless I have to. And if I do have to 
implement the noise types myself then I perhaps I don't even need Wand. 
It might be the case that all the noise types can be implemented 
using just `cv2`, `numpy`, and `pillow`.

#### Albumentations
Albumentations is a library meant for creating image augmentation pipelines.
It has many possibilities when it comes to adding noise including ones for weather
related noise. You can add snow, rain, fog, sunflares, and change the brightness plus
contrast. This is all great but the library is stochastic at its core meaning that
it's quite difficult to add the exact amount of noise that you want. For instance,
for the `RandomRain` augmentation, it's possible to set the slant of the rain drops,
their size, and their color but it's not possible to set the rain droplets positions
deterministically. Even if I seed the randomness, running the code again will change
the positions of the droplets.

However, there is also an option for functional transforms where you can specify every parameter. This is great but the functional transforms also require you to input a list of 
all the coordinates of snow, fog, rain particles which is not ideally what I want. But what I could do is generate a list of points of rain/snow using the `RandomRain` augmentation, save those points and then use them in the functional transforms. The only problem with this
approach is that I need to do this process for every image with different dimensions.

I might also just use the basic version of the library and disregard the fact that the results aren't reproducible. If you set the parameters to be the same, then the images will basically be the same. Consider the following two images that were generated with the same parameters:
![random_rain_1.png](random_rain_1.png "random_rain_1.png")
![random_rain_2.png](random_rain_2.png "random_rain_2.png")

The quality is the same, it's just that the raindrops appear in slightly different positions.

#### AugLy
AugLy is an augmentation library that can be used for text, image, and video data.
However, I don't see an easy way of adding weather related noise so I won't investigate
this library further.

#### imgaug
imgaug is a python augmentation library that in many ways are similar to Albumentations.
It's possible to create snowy landscapes, clouds, fog, rain, and snowflakes on images
just like in Albumentations. From what I've read, you can basically do the same things
in imgaug that you can in Albumentations but that Albumentations is faster. 

### Evaluating IQA metrics on Albumentations
Using Albumentations, I created two datasets based on the following image
![1.png](../../Code/1.png)

For the first dataset, I generated 100 images and progressively added more rain and reduced the brightness for each image. The first image, `0.png` barely had any rain and was quite bright and the last image, `99.png` had heavy rain and was significantly darker. 

I generated the second dataset by repeating the approach but used fog instead of rain.

The two generated datasets can be seen [here](https://drive.google.com/drive/u/0/folders/155pY1k8fm-afJmyVYLT5yO7qpStZbsqg) and [here](https://drive.google.com/drive/u/0/folders/1_zXvPNkyUc5EhJJvQxgU025B5fi9QcWn).

With this data, I ran every metric in `pyiqa` that I could get working and stored the results. This generated a large dictionary of dictionaries where the outer keys are metric names and the values are dictionaries mapping file names to scores. 

There are many ways of interpreting the results and I began with a rather naive implementation. I evaluated each metric by counting the number of correct rankings that it got. For instance, if the metric `hyperiqa` classified `0.png` to be the best, `1.png` to be the second best, and then incorrectly ranked all other images, then `hyperiqa` would get the score `2/100 = 0.02`. This is of course a non-optimal solution since it doesn't account for how close a ranking is to the correct one. Nonetheless, working with this implementation I got the results that can be seen [here](https://drive.google.com/drive/u/0/folders/1_zXvPNkyUc5EhJJvQxgU025B5fi9QcWn) and [here](https://drive.google.com/drive/u/0/folders/155pY1k8fm-afJmyVYLT5yO7qpStZbsqg). You can also see a shortened form of the results below.

```python
{
    "wadiqam_nr": 1.0,
    "arniqa-live": 0.32,
    "topiq_nr-flive": 0.31,
    "dbcnn": 0.3,
    "arniqa-csiq": 0.26,
    "topiq_iaa_res50": 0.24,
    "arniqa-flive": 0.23,
    "liqe_mix": 0.2,
    "nrqm": 0.19,
    "clipiqa+_rn50_512": 0.17,
    "tres-flive": 0.17,
    "arniqa-kadid": 0.15,
}
```
**Rainy**
```python
{
    "topiq_nr-spaq": 0.94,
    "wadiqam_nr": 0.73,
    "nima-spaq": 0.61,
    "nrqm": 0.58,
    "dbcnn": 0.43,
    "topiq_nr-flive": 0.43,
    "maniqa-kadid": 0.4,
    "cnniqa": 0.35,
    "nima-koniq": 0.34,
    "topiq_iaa": 0.34,
    "topiq_nr": 0.27,
    "arniqa-spaq": 0.25,
    "ilniqe": 0.22,
    "unique": 0.22,
    "arniqa-csiq": 0.21,
}
```
**Foggy**

Amazingly, `wadiqam_nr` got all of the rankings for the rainy images correct. It was so good that I double-checked its results to make sure that there wasn't a bug anywhere. It didn't perform as good on foggy images but still was second out of all metrics. Interestingly, `topiq_nr-spaq` performed best out of all metrics on foggy images but was fourth to last in performance on rainy images.

I should note that there are a few SOTA models missing in these results. Q-Align and Musiq are two recent model architectures for IQA that are supposed to have great performance. I tried including them in my code but I got problems with out of memory errors in Torch. The same thing happened when I ran them using the free version in Colab. I might upgrade to Colab+ to get more RAM.

The next thing I want to do is finding more sophisticated evaluation tools then my simple naive evaluation. I also want to find ways of running some of the other IQA models. 