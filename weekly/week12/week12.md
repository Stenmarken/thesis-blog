## Week 12 24-28 Mar

### Choice of NR-IQA metrics

There are in total 56 NR-IQA metrics in pyiqa that can be listed using the command:

```
nr_metrics = pyiqa.list_models(metric_mode='NR')
```

The following is a list of metrics I've chosen to exclude for various purposes:

- **uranker** since it's specialized for underwater IQA
- **qalign_4bit** and **qalign_8bit** since they are versions of QAlign
- **laion_aes** since it's an IAA (Image Aestethic Assessment) technique
- **brisque_matlab** and **niqe_matlab** since they are simply MATLAB implementations of **brisque** and **niqe**. 
- **topiq_nr-face** since it's specialized to facial images. 
- **arniqa**, **arniqa-clive**,**arniqa-spaq** since they are redudant. I only include the model trained on the FLIVE dataset. The reason being that FLIVE is the largest dataset with the most variety so FLIVE is chosen wherever possible. Otherwise, Koniq10k is chosen.
- **clipiqa**, **clipiqa+_rn50_512**, and **clipiqa+_vitL14_512**. I only include  **clipiqa**+.
- **liqe** as I include **liqe_mix** which is basically **liqe** but trained on more datasets.
- **musiq**, **musiq-spaq** since I include **musiq-paq2piq**
- **topiq_nr** and **topiq_nr-spaq** since I include **topiq_nr-flive**
- **tres** since I include **tres-flive**
- **topiq_iaa** and **topiq_iaa_res50** as they are both IAAs
- **inception_score** and **fid** are removed as they are meant for generated images.
- **nima**, **nima-koniq**, **nima-spaq** are removed as they are IAAs.
- **nrqm**. Arbitrary removal to reduce number of IQAs.
- **pi**. Arbitrary removal to reduce number of IQAs.
- **piqe**. Arbitrary removal to reduce number of IQAs.
- **cnniqa**. Arbitrary removal to reduce number of IQAs.
- **entropy**. Arbitrary removal to reduce number of IQAs.
- **Qualiclip**. Arbitrary removal to reduce number of IQAs.

Having removed all of the above leaves me with the following 17 metrics:

```
['arniqa-flive', 
'brisque', 
'clipiqa+',
'clipscore',
'dbcnn',  
'hyperiqa', 
'ilniqe', 
'liqe_mix', 
'maniqa', 
'musiq-paq2piq', 
'niqe','paq2piq',  
'qalign', 
'topiq_nr-flive', 
'tres-flive', 
'unique', 
'wadiqam_nr']
```
