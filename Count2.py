# this will count the amount of words in a sentence

# this function will split the sentence into words


def break_words(sentence):
    """This function will break up words for us."""
    words = sentence.split(' ')
    return words


print "Please write something."
sentence = raw_input(">: ")

print "This is your sentence: << %s >>" % sentence
print "Your sentence contains : %d words" % len(break_words(sentence))
print break_words(sentence)
