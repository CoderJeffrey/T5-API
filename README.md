# Overview 📑
A Module can be implemented to 
 1. get paraphrased text

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
#### spaCy 

- pip
- Conda (recommended - optional)
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


