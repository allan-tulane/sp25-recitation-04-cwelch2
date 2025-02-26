# recitation-04

from collections import defaultdict
from operator import add


#### PART ONE ###

def run_map_reduce(map_f, reduce_f, docs):
    # done. do not change me.
    """    
    The main map reduce logic.
    
    Params:
      map_f......the mapping function
      reduce_f...the reduce function
      docs.......list of input records
    """
    # 1. call map_f on each element of docs and flatten the results
    # e.g., [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1), ('sam', 1), ('is', 1), ('ham', 1)]
    pairs = flatten(list(map(map_f, docs)))
    # 2. group all pairs by their key
    # e.g., [('am', [1, 1]), ('ham', [1]), ('i', [1, 1]), ('is', [1]), ('sam', [1, 1])]
    groups = collect(pairs)
    # 3. reduce each group to the final answer
    # e.g., [('am', 2), ('ham', 1), ('i', 2), ('is', 1), ('sam', 2)]
    return [reduce_f(g) for g in groups]

def word_count_map(doc):
    """
    Params:
      doc....a string to be split into tokens. split on whitespace.
    Returns:
      a list of tuples of form (token, 1), where token is a whitespace delimited element of this string.
      
    E.g.
    >>> word_count_map('i am sam i am')
    [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1)]
    """
    splitDoc = doc.split()              # split doc before counting words
    returnList = []                     # empty list to append and return to
    for word in splitDoc:               # iterate through the doc, adding each word with the form (word, 1) to the list
        returnList.append((word, 1))
    return returnList                   # return results


def word_count_reduce(group):
    """
    Params:
      group...a tuple of the form (token, list_of_ones), indicating the number of times each word appears.
    Returns:
      tuple of form (token, int), where int is the number of times that token appears
    E.g.
    >>> word_count_reduce(['i', [1,1]])
    ('i', 2)
    
    NOTE: you should use call the `reduce` function here.
    """
    return (group[0], reduce(add, 0, group[1]))


def iterate(f, x, a):
    # done. do not change me.
    """
    Params:
      f.....function to apply
      x.....return when a is empty
      a.....input sequence
    """
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])
    
def flatten(sequences):
    # done. do not change me.
    return iterate(plus, [], sequences)

def collect(pairs):
    """
    # done. do not change me.
    Implements the collect function (see text Vol II Ch2)
    E.g.:
    >>> collect([('i', 1), ('am', 1), ('sam', 1), ('i', 1)])
    [('am', [1]), ('i', [1, 1]), ('sam', [1])]    
    """
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())


def plus(x, y):
    # done. do not change me.
    return x + y

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        return f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
    
    

### PART TWO ###

def sentiment_map(doc,
                  pos_terms=set(['good', 'great', 'awesome', 'sockdolager']),
                  neg_terms=set(['bad', 'terrible', 'waste', 'carbuncle', 'corrupted'])):
    """
    Params:
      doc.........a string to be split into tokens. split on whitespace.
      pos_terms...a set of positive terms
      neg_terms...a set of negative terms
    Returns:
      a list of tuples of form (positive, 1) or (negative, 1)      
    E.g.
    >>> sentiment_map('it was a terrible waste of time')
    [('negative', 1), ('negative', 1)]
    """
    posTuple = ('positive', 1)              # tuple for positive words
    negTuple = ('negative', 1)              # tuple for negative words
    returnList = []                         # empty list to append to and return
    splitDoc = doc.split()                  # split doc before checking for positive and negative words

    for word in splitDoc:                   # iterate over all words in doc
        if word in pos_terms:
            returnList.append(posTuple)     # add positive tuple to returnList if word is in list of positive words
        elif word in neg_terms:
            returnList.append(negTuple)     # add negative tuple to returnList if word is in list of negative words
    return returnList                       # return results


