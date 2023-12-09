# DSC180A Google Street View 
This is the first part of the senior capstone. This project uses Google Street View to collect the images for the dataset. In conjuction with labellbox the images uses object detection to train a DeTr HuggingFace model to label SDG&E equipment such as poles and transformers. 

# Part 1 Collection and Labelling

## Image collection 
Using the Google Street View api I acquired imgages of 5 transformers and 5 poles from around San Diego at different zooms and angles totaling in 150 images. I wrote the script in a Jupyter notebook and that includes functions that call the api to collect, name, and save images. Including supplementary functions that allow the image to be properly attained using a digital signature.
## Labeling and Object Detection
After collecting the images I used labellbox to classify the fixtures for detection as poles or underground structures. 

# Part 2 Fine tuning A DeTr Model and Collaboration

## 