# SARS-CoV-antivirals-DeepChem
Prediction of new possible antivirals for SARS-CoV type viruses using DeepChem API. This prediction is based on the idea that the main protease Mpro of SARS-CoV is very similar to the SARS-CoV-2 protease. Different deep learning classifiers are trained using known inhibitors of SARS-CoV Mpro to predict antivirals in a natural products database.

In the folder named "datasets" you can find the data used to train the models as well as the data for making predictions.
The folder "features_antivirals" contains the features calculated with each DeepChem featurizer for the known inhibitors of Mpro.
The folder "features_predictions" contains the features calculated for the natural products database with the DeepChem featurizer to use the best model.
In the folder "models" you can find the best model trained, showing AUROC = 0.774.
The folder "predictions" contains a csv with the predicted molecules showing the probability of being an antiviral.
The script "augmentation.py" was used to perform data augmentation with the initial SMILES.
The code to obtain the model and the predictions is provided in a jupyter notebook intended to be run in colab.

This project was developed as a master's degree in bioinformatics final project (the thesis is provided in Spanish as a pdf).