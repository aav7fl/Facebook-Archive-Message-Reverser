####################################
# File name: parser.py             #
# Author: Kyle Niewiada, anonymous #
# Date created: 2015, October 09   #
# Date modified: 2015, October 17  #
# Python version: 2.7              #
####################################
from bs4 import BeautifulSoup
import sys

def reverse_messages(soup):
    divOfThreads = list(soup.select('.contents > div'))

    """for each group of divs containing <div class="thread">"""
    for div in range(0, len(divOfThreads)):

        """for each thread of messages inside each div"""        
        for threadDiv in range (0, len(divOfThreads[div].select('.thread'))):
        
            """select all the messages inside each thread"""
            p = list(divOfThreads[div].select('.thread')[threadDiv])[::-1]
            
            """encode to UTF-8 to prevent Unicode errors"""
            q = [x.encode('utf-8') for x in p]

            length = len(q)

            """now reverse all message pairs inside the current thread"""
            for x in range(0, length-1, 2):
                q[x], q[x+1] = q[x+1], q[x]

            """append the reversed message order to the messages_reversed.html file"""
            reversedHTMLFile = open('messages_reversed.html', 'a')
            reversedHTMLFile.write('\n'.join(q))
            reversedHTMLFile.close()

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("USAGE: %s [HTML FILE]" % sys.argv[0])
        sys.exit(1)
    
	"""parse the HTML file from the command line argument with BeautifulSoup"""	
    soup = BeautifulSoup(open(sys.argv[1]), "html.parser")
    
    """re-create messages_reversed.html file for writing"""
    reversedHTMLFile = open('messages_reversed.html', 'w')
    reversedHTMLFile.close()
    
    """pass the parsed file to reverse the messages"""
    reverse_messages(soup)

    print("Done")
