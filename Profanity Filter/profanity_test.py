import urllib

def read_text():
    quotes = open("/Users/cblacksher/Desktop/movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Woah There Man")
    elif "false" in output:
        print("You're Good")
    else:
        print("Something went wrong")
read_text()
