### pyiqa

pyiqa is a python package that includes many implementations of modern IQA methods.

pyiqa has the following models incldued
```python
>>> pyiqa.list_models()
['ahiq', 'arniqa', 'arniqa-clive', 'arniqa-csiq', 'arniqa-flive', 'arniqa-kadid', 'arniqa-live', 'arniqa-spaq', 'arniqa-tid', 'brisque', 'brisque_matlab', 'ckdn', 'clipiqa', 'clipiqa+', 'clipiqa+_rn50_512', 'clipiqa+_vitL14_512', 'clipscore', 'cnniqa', 'cw_ssim', 'dbcnn', 'dists', 'entropy', 'fid', 'fsim', 'gmsd', 'hyperiqa', 'ilniqe', 'inception_score', 'laion_aes', 'liqe', 'liqe_mix', 'lpips', 'lpips+', 'lpips-vgg', 'lpips-vgg+', 'mad', 'maniqa', 'maniqa-kadid', 'maniqa-pipal', 'ms_ssim', 'msswd', 'musiq', 'musiq-ava', 'musiq-paq2piq', 'musiq-spaq', 'nima', 'nima-koniq', 'nima-spaq', 'nima-vgg16-ava', 'niqe', 'niqe_matlab', 'nlpd', 'nrqm', 'paq2piq', 'pi', 'pieapp', 'piqe', 'psnr', 'psnry', 'qalign', 'qalign_4bit', 'qalign_8bit', 'ssim', 'ssimc', 'stlpips', 'stlpips-vgg', 'topiq_fr', 'topiq_fr-pipal', 'topiq_iaa', 'topiq_iaa_res50', 'topiq_nr', 'topiq_nr-face', 'topiq_nr-flive', 'topiq_nr-spaq', 'tres', 'tres-flive', 'unique', 'uranker', 'vif', 'vsi', 'wadiqam_fr', 'wadiqam_nr']
```

A full 82 different models that can be used for IQA. Not all of these are suited to the task in the thesis though as many are Full Reference models, i.e. they compare a distorted image with a reference image. In self-driving, we do not have the luxury of being able to compare the captured images with non-distorted reference images so we have to make due with No Reference IQA.

I also have problems running some of the models due to configuration or hardware issues. Running `qalign`, `qalign_4bit`, and `qalign_8bit` caused `torch.OutOfMemory` issues on my computer and I got various issues trying to run `clipiqa+, entropy, hyperiqa, laion_aes, musiq, musiq-ava, musiq-paq2piq, musiq-spaq, paq2piq`. I'll sort the issues out for these models if I need it in the future.

Anyway, I used the remaining models that did work
```python
['wadiqam_nr', 'ilniqe', 'hyperiqa', 'arniqa-clive', 'arniqa-csiq', 'arniqa-flive', 
 'arniqa-kadid', 'arniqa-live', 'arniqa-spaq', 
 'arniqa-tid', 'brisque_matlab', 'clipiqa', 'clipiqa+', 
 'clipiqa+_rn50_512', 'dbcnn', 'cnniqa', 'liqe', 'liqe_mix',
 'maniqa', 'maniqa-kadid', 'maniqa-pipal', 
 'nima', 'nima-koniq', 'nima-spaq', 'nima-vgg16-ava', 'niqe', 
 'niqe_matlab', 'nrqm', 'pi', 'piqe',
 'topiq_iaa', 'topiq_iaa_res50', 'topiq_nr', 
 'topiq_nr-flive', 'topiq_nr-spaq', 'tres', 'tres-flive', 'unique']
```

using the `sample_imgs` dataset which consists of roughly 100 images from the DeepLearning_Winter23_Collection10_Drive11_HilantiePohjoiseen data set, a few compressed version of images in the data set (which caused problems due to dimensionality), and a few calibration images of very sharp and blurry images.

The results can be seen [here](https://github.com/Stenmarken/image-quality-assessment/blob/main/test-pyiqa/sample_images.json). I haven't gone through the results in any great detail since there's so much data to comb through. I probably need to create a much smaller dataset of only a few images to be able to compare methods.