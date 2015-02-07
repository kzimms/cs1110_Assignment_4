# a4.py
# Kathryn Zimmerman (kpz8) and Max Senkovsky (mgs253)
# 2 November 2014
""" Functions for Assignment A4"""


# Task 1: Word Lists

def build_word_list(filename):
    """Returns a list of words from the given file
    
    Each word in the file should stored on a separate line. The lines are trimmed 
    to remove trailing spaces and line returns. 
    
    Example: build_word_list('short.txt') returns the 10 element list of words
    ['the','be','to','of','and','a','in','that','have','it'].
    
    Precondition: filename is the name of a text file storing a list of words.
    
    Enforced Precondition: filename is a string"""
    
    assert type(filename) == str, `filename`+'is not type str'
    
    file = open(filename)
    
    wordlist = []
    
    for line in file:
        
        if line.find('\n') == -1:
            wordlist.append(line)
            
        else:
            wordlist.append(line[:-1])
        
    file.close()
    return wordlist
    

def word_list_by_size(words, size):
    """Returns the elements of words that have length size
    
    The words in the resulting list should be in the same order as the original list.
    
    Example: word_list_by_size(['a', 'at', 'axe', 'by'], 2) returns ['at','by']
    
    Precondition: words is a list of strings. size is a positive int.
    
    Enforced Precondition: words a list. size is a positive int."""
    
    assert type(words) == list
    assert type(size) == int
    assert size > 0 
    result = []
    
    for x in words:
        if len(x) == size:
            result.append(x)
    
    return result


def word_list_extend(words, prefix):
    """Returns the word list that is the result of adding prefix to the start of 
    every word in the list words.
    
    The resulting word list is sorted alphabetically.
    
    Example: word_list_extend(['at', 'rap'], 'c') returns ['cat', 'crap'].
    
    Precondition: words is a list of strings. prefix is a string.
    
    Enforced Precondition: words is a list. prefix is a string."""
    
    assert type(words) == list
    assert type(prefix) == str
    
    result = []
    
    for x in words:
       new = prefix + x
       result.append(new)
       
    result.sort()
    
    return result


# Task 2: Prefix Maps

def pmap_add_word(pmap,word):
    """Adds a single word to a prefix map.
    
    This is a procedure.  It modifies the contents of pmap. It does not return.
    a new prefix map.  
    
    This function will add the word AND all of its prefixes to pmap.  For each
    prefix it will add the next letter to the list of values.  For the complete word, 
    it will add '' to the list of values. 
    
    This function does not add duplicates to the prefix map.  If a letter is already
    in the list for a given prefix map, then it will not add it a second time.
    
    Example: If pmap is the empty map {}, then pmap_add_word(pmap,'at') changes
    pmap to the dictionary { '':['a'], 'a':['t'], 'at':[''] }.

    Example: If pmap is { '':['a'], 'a':['t'], 'at':[''] }, pmap_add_word(pmap,'as') 
    changes pmap to { '':['a'], 'a':['s', 't'], 'at':[''], 'as':[''] }.
    
    Precondition: pmap is a prefix map.  word is a string with only letters.
    
    Enforced Precondition: pmap is a dict. word is a string with only letters."""
    
    assert type(pmap) == dict
    assert type(word) == str
    assert word.isalpha()
    
    wl = list(word)
    length = len(wl)
    
    for k in range(length-1):
        if ''.join(wl[:k+1]) in pmap:
            pmap[''.join(wl[:k+1])].append(wl[k+1])
        else:
            pmap[''.join(wl[:k+1])] = [wl[k+1]]
            
    if '' in pmap and wl[0] not in list(pmap['']):
        pmap[''].append(wl[0])
    if '' not in pmap:
        pmap[''] = [wl[0]]
        
    if word in pmap:
        pmap[word].append('')
    else:
        pmap[word] = ['']
    

def word_list_to_pmap(words):
    """Returns the prefix map for the given word list.
    
    Hint: pmap_add_word is a useful helper function.
    
    Precondition: words is a list of strings with only letters.
    
    Enforced precondition: words is a list."""
    
    assert type(words) == list
    
    pmap = {}
    
    for x in words:
        pmap_add_word(pmap,x)
        
    return pmap


def pmap_to_word_list(pmap):
    """Returns the word list for the given prefix map.
    
    The word list should contain only those prefixes which have a next character
    of '' (the empty string) in the prefix map.
    
    Precondition: pmap is a prefix map.
    
    Enforced Precondition: pmap is a dict."""
    
    assert type(pmap) == dict
    
    wordlist = []
    
    for k in pmap:
        if '' in list(pmap[k]):
            wordlist.append(k)
    return wordlist


def pmap_has_word(pmap,word):
    """Returns True if word is in the prefix map.
    
    Precondition: pmap is a prefix map.  word is a string.
    
    Enforced Precondition: pmap is a dict. word is a string."""
    
    assert type(pmap) == dict
    assert type(word) == str
    
    wl = pmap_to_word_list(pmap)
    
    if word in wl:
        return True


# PART C: Word Completions

def autocomplete(prefix, pmap):
    """Returns the list of all words the complete prefix in pmap
    
    If there are no words completing prefix in pmap, this function returns the
    empty list.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    autocomplete('th',pmap) returns the list ['the', 'that'].  
    Similarly, autocomplete('x',pmap) returns the empty list []
    
    Precondition: prefix is a string that is either empty or has only letters. 
    pmap is a prefix map.
    
    Enforced Preconditions: We enforce the preconditions for prefix, but only
    enforce that pmap is a dict."""
    
    assert type(prefix) == str
    assert prefix.isalpha() or len(prefix)==0
    assert type(pmap) == dict
   
    temp = []

    if prefix not in pmap:
        return []
    
    if prefix in pmap:    
        for x in pmap[prefix]:
            if x == '':
                temp.append(prefix)
            else:
                temp = temp + autocomplete(prefix +x, pmap)
    for k in range(len(temp)-1):
        if temp[k] in temp[k+1:]:
            temp.remove(temp[k])
    if temp[-1] in temp[:len(temp)-1]:
        temp.remove(temp[-1])
    
    return temp


    
# PART D: Scrabble Puzzles

def scrabble(rack,size,pmap):
    """Returns the list of all valid words that you can form from the tile rack
    using EXACTLY size letters.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    scrabble('theob',2,pmap) returns ['be', 'to'].
    
    Precondition: rack is a string that is either empty or has only letters. 
    size is a positive integer. pmap is a prefix map.
   
    Enforced Precondition: We enforce the complete precondition for rack and size.
    We only enforce that pmap is a dict."""

    assert size > 0
    
    return scrabble_helper('',rack,size,pmap)


def scrabble_helper(prefix,rack,size,pmap):
    """"Returns the list of all valid words extending prefix that you can form from
    the tile rack using EXACTLY size ADDITIONAL letters.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    scrabble_helper('t','heob',1,pmap) returns ['to'], while 
    scrabble_helper('t','heob',2,pmap) returns ['the']

    Precondition: prefix and rack are a strings with only letters, but which may
    be empty. size is a nonnegative integer. pmap is a prefix map.
   
    Enforced Precondition: We enforce the complete precondition for prefix, rack, 
    and size. We only enforce that pmap is a dict."""
    
    assert type(rack) == str
    assert rack.isalpha() or len(rack)==0
    assert type(prefix) == str
    assert prefix.isalpha() or len(prefix)==0
    assert type(pmap) == dict
    assert type(size) == int
    assert size >= 0
    
    temp = []
    r2 = list(rack)
    for x in list(pmap[prefix]):
        
        if '' in list(pmap[prefix]) and size == 0:
            temp.append(prefix)
        if x in r2 and len(r2) != 0 and size != 0:
            r2.remove(x)
            temp.append(''.join(scrabble_helper(prefix + x ,\
                            ''.join(r2),int(size-1),pmap)))
    
    if temp == ['']:
        return []
    else:
        return temp


def match(template,pmap):
    """Returns the list of all valid words that match the given template.
    
    A template is a string combining letters and the '?' character.  A
    word is a match of for a template if it is the same length, and agrees
    with the template on every character that is not '?'. For example,
    'ate' matches the template 'a?e', as does 'axe'.
    
    The prefix map pmap is used to determine whether or not a word is valid.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    match('i?',pmap) returns ['in', 'it'].
    
    Precondition: template is a string of letters and '?'. pmap is a
    prefix map.
    
    Enforced Precondition: template is a string. pmap is a dict."""
    
    return match_helper('',template,pmap)


def match_helper(prefix,template,pmap):
    """Returns the list of all valid words that start with the given prefix, and
    whose remaining letters match the given template.
    
    Unlike match, the template in this case is not supposed to match the whole
    string. It is only supposed to match the remaining part of the string after
    the prefix.
    
    Example: If pmap is the prefix map created from 'short.txt', then 
    match_helper('i','?',pmap) returns ['in', 'it'].
    
    Precondition: prefix is a string of letters or empty. template is either empty or
    string of letters and '?'. pmap is a prefix map.
    
    Enforced Precondition: prefix is a string of letters or empty. template is a string. 
    pmap is a dict."""
    
    assert type(template) == str
    assert type(pmap) == dict
    assert type(prefix) == str
    assert prefix.isalpha() or len(prefix) == 0
    
    temp = []

    t2 = list(template)
    a = len(t2)
    for x in list(pmap[prefix]):
        
        if len(t2) > 1 and x == t2[0]:
            return match_helper(prefix + x, ''.join(t2[1:]),pmap)
        if len(t2) > 1 and t2[0] == '?':
            temp = temp + match_helper(prefix + x, ''.join(t2[1:]),pmap)
        if len(t2) == 1 and t2[0] == '?':
            temp = temp + match_helper(prefix + x,'',pmap)
        if len(t2) == 1 and x == t2[0]:
            temp.append(''.join(match_helper(prefix + x,'',pmap)))
        if len(t2) == 0 and x == '':
            temp.append(prefix)
    for k in range(len(temp)-2):
        if temp[k] in temp[k+1:]:
            temp.remove(temp[k])
        if len(temp[k]) < len(temp[k+1]):
            temp.remove(temp[k])
        if len(temp[k]) > len(temp[k+1]):
            temp.remove(temp[k+1])
    
  
    return temp