### Results of IQA techniques on 0-100 rain noise

In this experiment, 100 versions of the same image is captured with progressively increasing rain noise. The exact noise of each of the versions can be found [here](file_to_config.json).

The resulting scores, SPRCSs, and Kendall's tau can be found at the links below. `liqe_mix` was excluded from the experiment because it hung the execution `qualiclip` and `qualiclip+` were excluded since they weren’t in the release of torch-iqa that I have.

- [Scores](rainy_0_100.json)
- [SPRCCs](rainy_0_100_spearman.json)
- [Kendall's tau](rainy_0_100_kendall.json)
- [Qalign scores](rainy_qalign.json)
- [Images](https://drive.google.com/drive/folders/1oy_aiSvZ8JjGJnJWKNzPPQr2nCgpMlTi?usp=sharing)
