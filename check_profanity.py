import sys
import urllib.request

if sys.version_info[0] >= 3:
    from urllib import request
    print("Python 3")
else:
    print("Python 2")

#TODO: This file doesnot work with Python 3.

##if sys.version_info[0] >= 3:
##    from urllib import request
##else:
##    # Not Python 3 - today, it is most likely to be Python 2
##    # But note that this might need an update when Python 4
##    # might be around one day
##    from urllib import request

def read_text():
    quotes =open("G:\Online Courses\DataScience@Udacity\python\python_udacity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check) :
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    
    connection.close()
    if "true" in output :
        print("Profanity Alert!")
    elif "false" in output :
        print("No curse word in this document.")
    else :
        print("Couldn't open properly.")
read_text()
