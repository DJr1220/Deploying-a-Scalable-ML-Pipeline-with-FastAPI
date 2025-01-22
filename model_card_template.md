# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The Model used is RandomForestClassifier from Sklearn

## Intended Use
The model takes 1994 cenus data on an individual, and predicts thier salary range.

## Training Data
The data used was from a csv called Census.csv
14 Features and 32561 Rows

Features: age, workclass, fnlgt, education, education-num, marital-status, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country, salary

## Evaluation Data
The data was 75-25 split using 75 % of the data as training set and 25% as the test set.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

Precision: 0.7416 | Recall: 0.6171 | F1: 0.6737

## Ethical Considerations
This data is used on what was reported at time of census. to using this data for finacial validation or planing more testing for Bias would need to take place. 

## Caveats and Recommendations
The data is over 30 years old. Data was cleaned using ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)) conditions to get a usable set of data.