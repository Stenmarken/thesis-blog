### Results of IQA techniques on 0-100 fog noise

In this experiment, 100 versions of the same image is captured with progressively increasing fog noise. The exact noise of each of the versions can be found [here](file_to_config.json).

The resulting scores, SPRCSs, and Kendall's tau can be found at the links below. `liqe_mix` was excluded from the experiment because it hung the execution `qualiclip` and `qualiclip+` were excluded since they weren’t in the release of torch-iqa that I have.

- [Scores](foggy_0_100.json)
- [SPRCCs](foggy_0_100_spearman.json)
- [Kendall's tau](foggy_0_100_kendall.json)
- [Qalign scores](foggy_qalign.json)
- [Images](https://drive.google.com/drive/folders/197ZE6O3BmOZEaEx-pr3CzRgk60PyadY_?usp=sharing)
