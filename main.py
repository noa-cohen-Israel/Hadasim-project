from word2number import w2n

class File_details():

    def __init__(self,file_path):
        self.__file_name=file_path.split("/")[-1]
        self.__word_dict=None
        with open(file_path) as file:
            self._file_lines = file.readlines()

    ## help function
    def __create_dict_words(self):
        """
        The function creates a dictionary of the words in the file and the number of times they appear in the file
        """
        self.__word_dict=dict()
        for line in self._file_lines:
            for word in line.split():
                word=word.lower()
                self.__word_dict[word] = self.__word_dict[word] + 1 if word in self.__word_dict else 1
    # ex 1
    def number_rows(self):
        """
        :return: Numbers of rows in the file
        """
        return len(self._file_lines)
    # ex 2
    def number_words(self):
        """
        :return:Numbers of words in the file

        """
        num_words=0
        for line in self._file_lines:
            num_words+=len(line.split())
        return num_words
    # ex 3
    def number_specific_words(self):
        """
        :return:Numbers of specific words
        """
        if self.__word_dict==None:
            self.__create_dict_words()
        return len(self.__word_dict)
    # ex 4
    def max_and_average_len_sentence(self):
        """
        :return: The longest sentence length in a file, the average sentence length in a file
        """
        max_len=0
        num_sentence=0
        sum_len_sentence=0
        for line in self._file_lines:
            len_sentence = len(line.split())
            sum_len_sentence+=len_sentence
            max_len=len_sentence if len_sentence>max_len else max_len
            num_sentence+=1
        return max_len,sum_len_sentence//num_sentence
    #  ex 5
    def popular_word(self):
        """
        :return: The most popular words
        """
        if self.__word_dict==None:
            self.__create_dict_words()
        popular_words=[]
        num_of_word=0
        for word in self.__word_dict.keys():
            if self.__word_dict[word]>num_of_word:
                num_of_word=self.__word_dict[word]
                popular_words=[word]
            elif self.__word_dict[word]==num_of_word:
                popular_words.append(word)
        return popular_words
    # ex 6
    def max_sequence_words_not_contain_k(self):
        """
        :return:The longest word sequence in a text that does not contain the letter k
        """
        max_sequence,sequence="",""
        max_words,sum_words=0,0
        for line in self._file_lines:
            for word in line.split():
                if 'k' in word.lower():
                    if sum_words > max_words:
                        max_sequence = sequence
                        max_words=sum_words
                    sequence=""
                    sum_words=0
                else:
                    sequence+=word+" "
                    sum_words+=1
            sequence+="\n"
        max_sequence = sequence if sum_words > max_words else max_sequence
        return max_sequence

    # ex 7
    def max_num(self):
        """
        :return: The largest number,in its numerical configuration or in words.
        """
        max=float('-inf')
        for line in self._file_lines:
            for word in line.split():
                if word.isdigit():
                    max=int(word) if int(word) > max else max
            try:
                num=w2n.word_to_num(line)
                max=num if num > max else max
            except:
                pass
        return max



