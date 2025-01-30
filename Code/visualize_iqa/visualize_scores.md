## Visualizing IQA scores
Here are the results from plotting the results from the IQA evaluations on the rainy and foggy images. The x-axis is the severity level of the added noise. The scores have been standardized using the `StandardScaler` method from `scikit-learn`. It standardizes the data so it has 0 mean and 1 in standard deviation.

**Note that 99 in noise does not mean that the image consists of 99% noise or that 0 has 0% noise! Image 0 is simply the image with least noise while 99 is the image with the most. These images can be seen further down.**

### IQA results on rainy images

Rainy image `0.png` and `99.png` looks like this:
![](rainy_plots/0.png)
![](rainy_plots/99.png)

![](rainy_plots/arniqa-csiq_arniqa-flive_arniqa-kadid_arniqa-live.png)
![](rainy_plots/arniqa-spaq_arniqa-tid_brisque_matlab_clipiqa.png)
![](rainy_plots/clipiqa+_clipiqa+_rn50_512_dbcnn_cnniqa.png)
![](rainy_plots/entropy_hyperiqa_2_laion_aes_musiq.png)
![](rainy_plots/liqe_liqe_mix_maniqa_maniqa-kadid.png)
![](rainy_plots/maniqa-pipal_nima_nima-koniq_nima-spaq.png)
![](rainy_plots/musiq-ava_musiq-paq2piq_musiq-spaq_paq2piq.png)
![](rainy_plots/nima-vgg16-ava_niqe_niqe_matlab_nrqm.png)
![](rainy_plots/pi_piqe_topiq_iaa_topiq_iaa_res50.png)
![](rainy_plots/topiq_nr_topiq_nr-flive_topiq_nr-spaq_tres.png)
![](rainy_plots/tres-flive_unique_clipiqa+_vitL14_512_clipiqa+_2.png)
![](rainy_plots/wadiqam_nr_ilniqe_hyperiqa_arniqa-clive.png)

### IQA results on foggy images
Foggy image `0.png` and `99.png` looks like this: 
![](foggy_plots/0.png)
![](foggy_plots/99.png)


![](foggy_plots/arniqa-csiq_arniqa-flive_arniqa-kadid_arniqa-live.png)
![](foggy_plots/arniqa-spaq_arniqa-tid_brisque_matlab_clipiqa.png)
![](foggy_plots/clipiqa+_clipiqa+_rn50_512_dbcnn_cnniqa.png)
![](foggy_plots/entropy_hyperiqa_2_laion_aes_musiq.png)
![](foggy_plots/liqe_liqe_mix_maniqa_maniqa-kadid.png)
![](foggy_plots/maniqa-pipal_nima_nima-koniq_nima-spaq.png)
![](foggy_plots/musiq-ava_musiq-paq2piq_musiq-spaq_paq2piq.png)
![](foggy_plots/nima-vgg16-ava_niqe_niqe_matlab_nrqm.png)
![](foggy_plots/pi_piqe_topiq_iaa_topiq_iaa_res50.png)
![](foggy_plots/topiq_nr_topiq_nr-flive_topiq_nr-spaq_tres.png)
![](foggy_plots/tres-flive_unique_clipiqa+_vitL14_512_clipiqa+_2.png)
![](foggy_plots/wadiqam_nr_ilniqe_hyperiqa_arniqa-clive.png)
