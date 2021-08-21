import pandas as pd
from nltk.corpus import wordnet


def get_content():
    with open('content.txt') as f:
        lines = f.read()
    return lines

def freq(string,limit):
    # break the string into list of words
    str_list = string.split()

    # gives set of unique words
    str_list=[i.lower() for i in str_list]
    unique_words = set(str_list)
    repeated_words=[]
    for words in unique_words:
        if str_list.count(words)>limit:#getting words having frequency greater than 1
            syns=[words] #if its not able to find its synonym, returns the word itself
            try:
                syns = wordnet.synset("{}.n.1".format(words)).lemma_names()
            except:
                pass
            repeated_words.append((words,str_list.count(words),syns))
    df=pd.DataFrame(repeated_words,columns=["word","frequency","synonyms"])
    df.to_csv("repeated_words.csv")


if __name__ == '__main__':
    resume_content_string=get_content()
    print("done reading")
    freq(resume_content_string,2)
    print("done execution")

