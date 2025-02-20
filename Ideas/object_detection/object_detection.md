### Object detection as a proxy of image quality

I started looking at ways of using object detection results as a way of setting ground truth values for image quality. At first glance, it seems easy and logical. As the images taken by an autonomous vehicle will be used by object detection systems in a ML-pipeline, it makes sense to evaluate the image based on if an object detection system can accurately detect the objects in it. It's then possible to create a scoring system based on the certainty of the object detection system. Lower certainty -> lower image quality score.

While this seems logical, there emerges a problem when you try to specify this more precisely. To see what I mean, consider the following two images:

![000188](000188.png_bounding_boxes.png)
![000192](000192.png_bounding_boxes.png)

The first image is taken moments before the second one meaning that the camera is further away from the cars in the scene. It is also less sure that the objects to the right are in fact cars. It's hard to see in the images, but the probabilties that the two objects to the right are cars are 0.78 and 0.77 for the first image and 0.85 and 0.87 for the second image. If we were to apply the rule outlined above where lower probability means that the image is worse, then we would clearly classify the second image as being better than the first. However, the images appear to have exactly the same quality. The only reason why the second image has higher probabilities in its bounding boxes appears to be that it's closer to the cars which makes it easier for the object detection algorithm. 

Another problem is that the object detection algorithm isn't perfect and it sometimes cannot see objects despite a good view. This can be seen in the pictures below:

![000141](000141.png_bounding_boxes.png)
![000142](000142.png_bounding_boxes.png)

The first picture is taken at timestamp 141 and in that picture the object detection can detect the car in the center of the image. In the second image, taken at timestamp 142, the object detection doesn't spot the car in the center. If I used object detection as a proxy for quality in this case, I would score the first image as better than the second one even though the images are basically the same.

This is something I have to consider when implementing this system and I don't know a good way around it. 
