# Overview 📑
A Module can be implemented to generate paraphrased text (based on T5) from all the text files in a specified directory.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
#### spaCy 
- pip
- Conda (recommended)
- spaCy   
  
  

#### T5 Paraphrase Generator
- Huggingface transformers library
- Pytorch
- Tensorflow 

### Prepare
```
npm install
```   

### General Usage
```
python output.py    
```   
Utilized API from T5 Transformers to get more sentences of the similar meaning of input sentencec.
- Read all text files from **TRAIN/NLI** dir
- Generate Paraphrases for all files in **TRAIN/NLI** dir
- Store the Paraphrases in **NLI_TRAIN_TOTAL** dir (grouped by agenda) (ADD Mode instead of OVERWRITE)

```
NLI_TRAIN_DATA File Structure
    - Agenda1
        - Trigger1.txt
        - Trigger2.txt
        - Trigger3.txt
    - Agenda2
        - Trigger4.txt
        - Trigger5.txt
    - Agenda3
```
(Results of all paraphrased sentences)

   
   
       
       

### Additional Info
To test the results of the work, use the following command:
```
python cl.py
```
- The demo file Use the demo sentence "Do you want to eat Pad Thai? There are really delicious food and I am sure you would like it."
- Print the 10 or less generated similar sentence in the console
