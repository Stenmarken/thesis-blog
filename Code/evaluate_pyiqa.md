### Evaluating pyiqa metrics

Now that I've got pyiqa metrics working I need to find a good way of evaluating them. One approach of evaluating the metrics is to take an image, create corrupted/distorted versions of the image, and then run the metrics on each of the distorted images. This way, it's possible to see how the score is affected by worsening the quality.

[imagecorruptions](https://github.com/bethgelab/imagecorruptions) is a library in python that can artificially add various kinds of noise to images. It has gaussian noise, motion blur, defocus blur, and a few more. The library is good to create distortions but its fundamental flaw is that the distortions have to specified on a 1-5 scale. Thus, from a generic image, it's only possible to get 5 versions of it with various levels of distortions. This is not great since we would ideally like to be able to have 100 or 1000 images with varying levels of distortion and see how that affects the metric scores.

In the future, it might be good to modify the library to handle more levels but we'll make due with the 5 levels for now.

I wrote some code that for three types of distortions (gaussian noise, motion blur, defocus blur) generates 5 distorted images for each distortion type with the level ranging from 1-5. Below are the 5 images with gaussian noise distortions going from best to worst.
![1.png](1.png_gaussian_noise_1.png "something")
![1.png](1.png_gaussian_noise_2.png "something")
![1.png](1.png_gaussian_noise_3.png "something")
![1.png](1.png_gaussian_noise_4.png "something")
![1.png](1.png_gaussian_noise_5.png "something")

With the distorted images I then run every available metric that I could get working and see what the score is. The results can be found here: [link](https://github.com/Stenmarken/image-quality-assessment/blob/main/test-pyiqa/corrupted/results.json)
