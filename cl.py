from src.T5_Generator.output import Generate_Paraphrase

def T5(lines):
    #generate the Paraphrases Sentences by T5
    para = []
    Phrase_Generator = Generate_Paraphrase()
    for line in lines:
        #get 10 or less paraphrased from T5
        para = Phrase_Generator.generate(line)

        #preprocess our paraphrased text
        for i in range(len(para)):
            print("original: ", line, "| Paraphrased: ",para[i])
    return para

if __name__ == "__main__":
    lines =  ["Do you want to eat Pad Thai? There are really delicious food and I am sure you would like it."]
    paraphrased_lines = T5(lines)
    