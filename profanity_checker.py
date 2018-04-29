import urllib
def read_text():
    quotes = open("/Users/ryanbowlen/Documents/Projects/Python Projects/ProfanityChecker/movie_quotes.txt")
    contents_of_file = quotes.read()
    print (contents_of_file+"\n")
    check_profanity(contents_of_file)
    quotes.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    #print(output)
    if "true" in output:
        print "Profanity alert!"
    elif "false" in output:
        print "This document has no curse words."
    else:
        print "Could not scan document properly."
    
read_text()
