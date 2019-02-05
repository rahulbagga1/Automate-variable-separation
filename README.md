# Automate variable separation 

This script will automatically separate the continuous variables and categorical variables and output names of the columns of each type.

Input contains the path of data file in csv (comma-separated-values) format and data should have correct datatypes assigned to each variable.

Second Input contains the value of 'threshold' variable in script. This variable is used to define threshold for ordinary variables to have minimum unique values in column. Preferable value for this variable should be 10 (integer only).

Output is the names of columns of each type.

The script works by comparing datatypes of each variable of data and is tested on many datasets.

Feel free to contribute to this code and I am most welcome for your suggestions.
