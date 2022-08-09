#system module
import os
from os.path import isfile, join, isdir

#path dir
cur_dir = os.path.dirname(__file__)
NLI_DATA_DIR = os.path.join(cur_dir, "Train", "NLI")

from src.T5_Generator.output import Generate_Paraphrase

#create a result directory
RESULT_DIR_NAME = "NLI_TRAIN_TOTAL"
try:
    os.makedirs(cur_dir+f'/{RESULT_DIR_NAME}')
except:
    pass

AGENDAS_LIST = [f for f in os.listdir(NLI_DATA_DIR) if isdir(join(NLI_DATA_DIR, f))]

from collections import defaultdict
trigger_map = defaultdict(list)

for agenda in AGENDAS_LIST:
    nli_path = join(NLI_DATA_DIR, agenda)
    try:
        os.makedirs(cur_dir+f'/{RESULT_DIR_NAME}/{agenda}')
    except:
        pass
    
    #first item is the name for trigger (payment.txt) -> payment is the trigger
    trigger_map[agenda] = [f.split('.')[0] for f in os.listdir(nli_path) if isfile(join(nli_path, f))]

def single_trigger(agenda, trigger):
    source_dir = join(NLI_DATA_DIR, agenda)
    lines = open(f"{source_dir}\\{trigger}.txt",'r').readlines()

    #generate the Paraphrases Sentences by T5
    Phrase_Generator = Generate_Paraphrase()

    trig = open(f"{RESULT_DIR_NAME}\\{agenda}\\{trigger}.txt","a")
    for line in lines:
        original_text = line.strip()
        trig.write(f"Original Text: {original_text} \n")
        
        #get 10 or less paraphrased from T5
        para = Phrase_Generator.generate(line)

        #preprocess our paraphrased text
        for i in range(len(para)):
            para[i] = para[i].strip()

        for paraphrases_text in para:
            trig.write(f"Paraphrase: {paraphrases_text}\n")
        trig.write(f"\n")
    trig.close()

def single_agenda(agenda):
    for trigger in trigger_map[agenda]:
        single_trigger(agenda, trigger)

def multiple_agendas():
    for agenda in trigger_map.keys():
        single_agenda(agenda)
    
if __name__ == "__main__":
    #single_trigger("get_contact_info","name")
    multiple_agendas()
    