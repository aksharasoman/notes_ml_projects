Eg:
 building a model to predict a specific type of rare allergic reaction. The challenge is that  dataset contains far more instances of patients without the allergy than those with it, causing  model to misclassify allergic patients as non-allergic frequently. Getting more data for such a rare allergy is difficult.

##### Strategies
- Augment the dataset with slightly modified copies of the patient data showing the allergy.
	- augmenting the underrepresented class.
- Assign a higher weight to the underrepresented classes in the loss function.
	- This method increases the penalty for the model if it misclassifies a sample from the rare class.
- oversampling the underrepresented classes 
- downsampling the dominant class
- creating additional synthetic data.

