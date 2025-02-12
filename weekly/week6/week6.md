### Week 6 - 10-15 Feb

I have left the world of IQA for the time being and started looking into PCQA methods.

While the field of PCQA is smaller than IQA, there exists quite a few no-reference methods.
Here is a list of a few promising ones I'm looking into. I'm still in the process
of writing the code for the PCQA-evaluation. The results of that will hopefully appear
on the blog shortly.

### MM-PCQA
[MM-PCQA](https://arxiv.org/abs/2209.00244) makes use of both the 3D structure of point
clouds and a 2D projection of the points to make quality assessments. The idea is to asses 
quality based on two modalities. The code is up on [GitHub](https://github.com/zzc-1998/MM-PCQA) and seems easy to use.

### IT-PCQA
[IT-PCQA](https://arxiv.org/abs/2112.02851) is similar to MM-PCQA in that it takes
insights from the image domain. It uses images as the source domain and point clouds
as the target domain. This means that it tries to transfer quality assessment of
images to quality assessment of point clouds. The reason for this is that assessing
image quality is much more straightforward than point cloud quality assessment. The model 
in the [GitHub](https://github.com/Qi-Yangsjtu/IT-PCQA) repo is trained on [SJTU-PCQA](https://vision.nju.edu.cn/28/fd/c29466a469245/page.htm),
a database of point clouds with mean opinion scores set by humans. The trouble is that
the point clouds are not similar to those that appear in autonomous driving. This
might be a recurring issue.

### LMM-PCQA
[LMM-PCQA](https://arxiv.org/pdf/2404.18203) uses a large multi-modality model to 
assess quality of point clouds. Much like IT-PCQA, LMM-PCQA uses 2D projections of
point clouds and assesses the quality of those projections. To compensate for the 
loss of information going from 3D -> 2D, the model extracts certain structural features
from the point cloud data.

### COPP-Net
[COPP-Net](https://arxiv.org/abs/2305.07829) divides the point cloud into smaller segments
and looks at the quality of those segments individually. For each segment, COPP-Net
determines texture features like variations in intensity, color, and patterns, as well 
as structural features like geometric properties of the points. It's possible that this 
method is too specific to detailed point clouds of objects up close. It remains to be seen
if it's appropriate for determining the quality of AV point clouds.