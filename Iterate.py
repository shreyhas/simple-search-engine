from _collections import defaultdict
import pandas as pd

class Iterate():
    """
    Iterates over .txt files, generates a dictionary, and then generates a reverse index
    """

    def __init__(self, no_of_docs):
        self.no_of_docs = no_of_docs
        pass


    def generate_dict(self):
        """
        make a dictionary for each word in the dataframe and associate locations with word
        :return: dictionary
        """
        dict = defaultdict(list)
        for i in range(self.no_of_docs-1):
            doc_txt = self.doc_to_df(i)
            #assign key to index in dictionary and its locations as tuples(docid,line,wordpos) as the values
            for j in range(len(doc_txt)):
                for k in range(doc_txt.shape[1]):
                    key = doc_txt[k][j]
                    dict[key].append((i,j,k))



    def doc_to_df(self, doc_no):
        """
        take the document and convert it into a df with indexes of line number
        :param doc_no: filename of document
        :return: doc_txt
        """
        doc_txt = pd.DataFrame()
        i = 1
        with open ('{doc_id}.txt'.format(doc_id = doc_no)) as file:
            for line in file:
                words = pd.Series(line.split(' '))
                doc_txt = doc_txt.append(words, ignore_index=True)
        return doc_txt


    def generate_reverse_index(self):
        """
        generate a reverse index using the content from the dictionary
        :return: reverse_index
        """
        pass



