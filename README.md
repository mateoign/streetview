# DSC180A Google Street View 
This is the first part of the senior capstone. This project uses Google Street View to collect the images for the dataset. In conjuction with labellbox the images uses object detection to train a DeTr HuggingFace model to label SDG&E equipment such as poles and transformers. 

## Data Sources
Data for this project is collected from [Google Street View Static API](https://developers.google.com/maps/documentation/streetview/overview). 

To run sunny.py, you need specifically structured JSON file. The JSON file will have 2 main item(OH and UG) and each should be the list of 5 different pole and within each pole, there should be 'loc' for lat and long 'heading' for heading direction of the image.

### Additional Files

Add various files located in the HDSI Capstone 2023-2024 Sharepoint Documents/Data folder to the data directory. This is needed in order to run `scripts/collect_images.py`:
* `joshua_structures.json`
* `kevin_structures.json`
* `jonathan_structures.json`
* `structure_coordinates.json`

## Setup

### Conda Environment
After cloning repo, navigating to root level and run:
```
conda env create -f environment.yml
```

### Credentials
Store credentials in `.env` file and load using [python-dotenv](https://pypi.org/project/python-dotenv/).

### Training Data
Create training data by running the following after setup is complete:
```
python scripts/collect_images.py
```

# Project Structure

```
├── data/               <- Local data files only (do not commit)
│
├── notebooks/          <- Jupyter notebooks
│
├── scripts/            <- Python scripts to run in command line
│
├── .env                <- Environment variables for the project
│
├── .gitignore          <- Git ignore file
│
├── environment.yml     <- Conda environment file
│
└── README.md           <- The top-level README for repo
```

Open the [finetune_detr notebook](https://github.com/mjignacio/dsc180a-streetview/blob/main/notebooks/finetune_detr.ipynb)
# Part 1 Collection and Labelling

## Image collection 
Using the Google Street View api I acquired imgages of 5 transformers and 5 poles from around San Diego at different zooms and angles totaling in 150 images. I wrote the script in a Jupyter notebook and that includes functions that call the api to collect, name, and save images. Including supplementary functions that allow the image to be properly attained using a digital signature.
## Labeling and Object Detection
After collecting the images I used labellbox to classify the fixtures for detection as poles or underground structures. 

# Part 2 Fine tuning A DeTr Model and Collaboration

## 
