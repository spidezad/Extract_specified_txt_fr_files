"""

    #############################################

     Module to extract portion of texts from a text file
     Author: Tan Kok Hua (Guohua tan)
     Email: spider123@gmail.com
     Revised date: May 17 2014

    ##############################################
    
    Module that extract user defined paragraph chuncks from a text file.

    Usage:
        User mark the start and end position of text required with specific symbol.
        Multiple marking can be done and can be specified by using overlap or non overlapping mode.
        Overlapping mode will use each subsequent symbol as end position as well as start position of next paragraph.
        Non Overlapping mode make even symbol index to be end position\
        so each pair of symbol index represent a paragraph to be extracted.

    TODO:
        enable regular expression instead of string.startwith function for symbol detection

    Updates:
        Jul 10 2014: Make changes to the non overlapping stop index. Rm the -1
                   : Add in dict as results.

    Bug:
        for line zero case..... not captured.
"""

def join_list_of_str(list_of_str, joined_chars= ''):
    """ Function to combine a list of str to one long str.
        Args:
            list_of_str (list): input list of str to join.

        Kwargs:
            joined_chars (str): character use to join the str.

        Returns:
            str: output str.

    """
    return joined_chars.join([n for n in list_of_str])

def manage_index_for_start_stop(index_list, overlapping):
    """ Function use to support sorting of start and end index by different mode (overlapping).
        Args:
            index_list (list): list of index (int) that pass in from para_extract function.
            overlapping (bool): same concept of the para_extraction function overlapping kwargs.
            
                1 - enable overlapping. The subsequent symbol will be the end of paragraph for first symbol\
                    and also use for start of the next paragraph
                0 - disable overlapping. the even index symbol will be used for the end of paragraph.
                    It will not be used for the start of next paragraph.
                    The next paragraph will be the next start symbol.
        Returns:
            start_index_list (list): contains all Start pt of the paragraph line.
            end_index_list (list): contains all end pt of paragraph line. (end line index)

    """
    if overlapping:
        ## the last symbol is taken to be the closing.
        start_index_list = index_list[:-1]

        ## end index,the corresponding enclosing index is taken to be len(next symbol) -1.
        ## Hence, end index list will not include the first symbol index.
        end_index_list = [n-1 for n in index_list[1:]]

    else:
        ## For non overlapping
        ## Start will be every odd index and end index will be every even index
        start_index_list = [index_list[n] -1 for n in range(len(index_list)) if n%2 == 0]
        end_index_list = [index_list[n] for n in range(len(index_list)) if n%2 == 1]

    ## For debugging -- uncomment to print index
##    print start_index_list
##    print end_index_list

    return start_index_list, end_index_list


def para_extract(filename, extract_symbol, overlapping =0 ):
    """ Function to extract series of paragraph from a txt file.
        Extraction is based on scanning the target symbol and\
        extracting the portion of text within the same symbol.
        User would need to specify symbol for the txt file or input certain identifier that points to the extaction.

        Args:
            filename (str): Input txt file name.
            extract_symbol (str): character to highlight start and end of extracting. (perfer special symbol eg @).

        Kwargs:
            overlapping (bool): determine the symbol extraction sequence.
                1 - enable overlapping. The subsequent symbol will be the end of paragraph for first symbol\
                    and also use for start of the next paragraph
                0 - disable overlapping. the even index symbol will be used for the end of paragraph.
                    It will not be used for the start of next paragraph.
                    The next paragraph will be the next start symbol.

        Note:
            User would need to ensure even number of symbol present.

        Returns:
            list: List of sentences str
            dict: dict with index on the list of sentences.
            
    """

    with open(filename,'r') as f:
        data = f.readlines()

    index_list = [n for n in range(len(data)) if data[n].startswith(extract_symbol)]

    start_index_list, end_index_list = manage_index_for_start_stop(index_list, overlapping)

    output_list_of_text = []
    output_dict_of_text = {}
    output_counter = 1
    for start, end in zip(start_index_list, end_index_list):
        output_list_of_text.append(join_list_of_str(data[start:end]))
        output_dict_of_text[output_counter] = join_list_of_str(data[start:end])
        output_counter =  output_counter +1 

    #print output_list_of_text

    return output_list_of_text, output_dict_of_text



if __name__ == '__main__':

    choice = [1]

    if 1 in choice:
        filename = r'C:\data\temp\htmlread_1.txt'
        key_symbol = '###'
        q,t = para_extract(filename, key_symbol, 0 )

    if 2 in choice:
        
        import nltk_tools
    
        for n in q:
            print nltk_tools.word_freq_summarize(n, adj_ratio =0.02 , min_sentences = 3)
    
