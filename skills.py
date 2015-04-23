from collections import Counter

# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    # For example:

    #     >>> print_dict(count_unique("each word appears once"))
    #     {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    # Words that appear more than once should be counted each time:

    #     >>> print_dict(count_unique("rose is a rose is a rose"))
    #     {'a': 2, 'is': 2, 'rose': 3}

    # It's fine to consider punctuation part of a word (e.g., a comma
    # at the end of a word can be counted as part of that word) and
    # to consider differently-capitalized words as different:

    #     >>> print_dict(count_unique("Porcupine see, porcupine do."))
    #     {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    #create a dict with empty values. print keys.
    # then count how many times a unique key is in string with for loop adding a coutner

    lst = string1.split(" ")


    # Can't do this, printing out collections.Counter type..
    # counted = Counter(lst)
    # print type(counted)


    dict_count_uniq = {}

    for word in lst:    
       
        if word not in dict_count_uniq:
            dict_count_uniq[word] = 1

        else:
            dict_count_uniq[word] += 1
        
    return dict_count_uniq

# sampleLst = "each word appears once"
# print count_unique(sampleLst)

sampleLst2 = "rose is a rose is a rose"
#print count_unique(sampleLst2)


# *********************************
def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    # For example:

    #     >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
    #     [1, 2]

    # If an item appears more than once in both lists, return it each
    # time:

    #     >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
    #     [1, 1, 2, 2]

    # (And the order of which has the multiples shouldn't matter, either):

    #     >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
    #     [1, 1, 2, 2]

    # """

    giantLst = list1 + list2

    giantSet = set(giantLst)
# ******** got stuck here (above) will redo later ********
# able to solve with if in below
# Not sure I understand this question

    common_num = []

    for num in list1 and list2:
        if num in list1 and list2:
            common_num.append(num)

    return common_num



    # print "giantLst", giantLst
    # return "giantSet", giantSet

sampleLst3 = [1, 2, 3, 4]
sampleLst4 = [1, 2]
sampleLst5 = [1, 1, 2, 2]

#return common_items(sampleLst3, sampleLst4)

# print common_items(sampleLst3, sampleLst5)

def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    # Just like `common_items`, this should find [1, 2]:

    #     >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
    #     [1, 2]

    # However, now we only want unique items, so for these lists, don't show
    # more than 1 or 2 once:

    #     >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
    #     [1, 2]

    # """


    set1 = set(list1) 
    #print set1
    set2 = set(list2)
    #print set2

    intersectionSet = set1 & set2
    #print intersectionSet
    return intersectionSet


    # print "giantLst", giantLst
    # return "giantSet", giantSet

sampleLst6 = [1, 2, 3, 4]
sampleLst7 = [1, 2]
sampleLst8 = [1, 1, 2, 2]

common_items(sampleLst6, sampleLst7)


# ******************************************************************************
def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    # For example:

    #     >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
    #     [[-2, 2], [-1, 1]]

    # This should always be a unique list, even if there are
    # duplicates in the input list:

    #     >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
    #     [[-2, 2], [-1, 1]]

    # Of course, if there are one or more zeros to pair together,
    # that's fine, too:

    #     >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
    #     [[-2, 2], [-1, 1], [0, 0]]

    """
    setFromList = set(list1)
    srtedList = sorted(setFromList)
    #print "sorted list", srtedList
  
    list_sum_zero = []

    for num in srtedList:
        if num + (-num) == 0:
            num_pair = [num, (-num)]
            #print num_pair
        # if num_pair[0] in list_sum_zero[num]:
        #     continue   
        if num_pair[1] in srtedList:
            list_sum_zero.append(num_pair)

    return list_sum_zero
 

  
sampleLst9 = [1, 2, 3, -2, -1]
sampleLst10 = [1, 2, 3, -2, -1, 1, 1]

#print sum_zero(sampleLst9)

## Can't figure out how to remove duplicate. Math logic is flawed. 
sum_zero(sampleLst10)



def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

    #     >>> sorted(find_duplicates(
    #     ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
    #     ['a', 'is', 'rose']

    # You should treat differently-capitalized words as different:

    #     >>> sorted(find_duplicates(
    #     ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
    #     ['Rose', 'a', 'is', 'rose']

    # """
    
    setFromList = set(words)
    uniqueList = list(setFromList)
    return uniqueList

sampleLst11 = "rose", "is", "a", "rose", "is", "a", "rose"
sampleLst12 = "Rose", "is", "a", "rose", "is", "a", "rose"


find_duplicates(sampleLst11)
find_duplicates(sampleLst12)


#************** Questions about this one. Can't get it as tuples answer format*******
def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    # For example:

    #     >>> word_length(["ok", "an", "apple", "a", "day"])
    #     [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    # """

    w_len = {}
    wordLen = []
    for word in words:
        tple = (word, len(word))
        wordCount = tple[1]
     

        ## WHY DOES THIS WORK AND NOT MY CODE BELOW! (str object has not attribute 'append')
        w_len.setdefault(wordCount, []).append(word)
        # if wordCount in w_len.keys():
        #     w_len[wordCount].append(word)
        #     print "this is supposed to be a blank value dict", w_len
        # else:
        #     w_len[wordCount] = word
        #     #w_len[wordCount] = wordCount

        # ALSO, I CANT GET THIS INTO A TUPLE AS THE DICTIONARY
    

    return w_len


sampleLst13 = "ok", "an", "apple", "a", "day"

# Failed at doing dictionary comprehension
word_length(sampleLst13)



def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    phrase_lst = phrase.split(" ")

    pirate_words = ["matey", "fleabag inn", "swabbie", "matey", "proud beauty", "foul blaggart", 
                    "galley", "yer", "arr", "swabbies", "be", "foul blaggart", "th'", "head", "me", "avast", "be", "matey"]

    normal_words = ["sir", "hotel", "student", "boy", "madam", "professor", "restaurant", "your", 
                    "excuse", "students", "are", "lawyer", "the", "restroom", "my", "hello", "is", "man"]

    pirate_dict = {}

    for index in range(len(pirate_words)):
        pirate_dict[normal_words[index]] = pirate_words[index]

    #return pirate_dict

    converted_phrase = []

    for word in phrase_lst:
        if word in pirate_dict:
            word = pirate_dict[word]
        converted_phrase.append(word)

    #for word in converted_phrase:

    #print converted_phrase
    #print type(converted_phrase)

    converted_phraseStr = ' '.join(converted_phrase)
    #print type(converted_phraseStr)

    return converted_phraseStr
    #print type(converted_phraseStr)

sampleLst14 = "my student is not a man"
sampleLst15 = "my student is not a man!"

#pirate_talk(sampleLst14)
pirate_talk(sampleLst15)


def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """




sampleLst16 = ["ok", "an", "apple", "a", "day"]

adv_word_length_sorted_words(sampleLst16)


##############################################################################
# You can ignore everything after here

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
