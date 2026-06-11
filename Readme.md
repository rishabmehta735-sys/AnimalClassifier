# Cat / Dog / Horse Classifier

A CNN built from scratch (trained on ~2.4k images) that predicts whether an image is a cat, dog, or horse, returning probabilities for each class.

A pre-trained model (`best_model.keras`) is included, so you can test it right away without retraining.

## Quick Start (use existing model)

```bash
streamlit run myApp.py
```

Upload an image and the app will display the predicted probabilities.

## Building Your Own Model

1. `python generateData.py` — scrape/generate raw images
2. Manually delete any images that aren't cats, dogs, or horses
3. `python cleanData.py` — clean the dataset
4. `python copyAndSplitDataset.py` — split into train/test sets
5. `python convertToRGB.py` — ensure all images are RGB
6. `python model.py` — define the model architecture
7. `python trainModel.py` — train the model
8. `python evaluateModel.py` — evaluate performance

## Requirements

- PIL
- tensorflow
- numpy
- random
- shutil
- streamlit