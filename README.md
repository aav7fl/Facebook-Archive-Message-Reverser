# Facebook Archive Message Reverser

## What is this?

This is a script developed by a friend and myself for a personal project that takes the entire messages.htm file from your [Facebook archive](https://www.facebook.com/help/212802592074644) (as of October 2015) and reverses the message order from descending to ascending. 

The Facebook message archive file presents you with groups of messages (when no CSS is used) approximately like this:

>Tom Smith, Bob Smith
>
>Tom SmithSaturday, 17 October 2015 at 12:45 EDT
>
>Hi Bob, I received your third message.
>
>Bob SmithSaturday, 17 October 2015 at 12:44 EDT
>
>Hey Tom, this is the third message I am sending.
>
>Tom SmithSaturday, 17 October 2015 at 12:43 EDT
>
>Hi Bob, I received your second message.
>
>Bob SmithSaturday, 17 October 2015 at 12:42 EDT
>
>Hey Tom, this is the second message I am sending.
>
>Tom SmithSaturday, 17 October 2015 at 12:41 EDT
>
>Hi Bob, I received your first message.
>
>Bob SmithSaturday, 17 October 2015 at 12:40 EDT
>
>Hey Tom, this is the first message I am sending.
>

However, the Python script rearranges the messages to look like this:

>Bob SmithSaturday, 17 October 2015 at 12:40 EDT
>
>Hey Tom, this is the first message I am sending.
>
>Tom SmithSaturday, 17 October 2015 at 12:41 EDT
>
>Hi Bob, I received your first message.
>
>Bob SmithSaturday, 17 October 2015 at 12:42 EDT
>
>Hey Tom, this is the second message I am sending.
>
>Tom SmithSaturday, 17 October 2015 at 12:43 EDT
>
>Hi Bob, I received your second message.
>
>Bob SmithSaturday, 17 October 2015 at 12:44 EDT
>
>Hey Tom, this is the third message I am sending.
>
>Tom SmithSaturday, 17 October 2015 at 12:45 EDT
>
>Hi Bob, I received your third message.
>
>Tom Smith, Bob Smith

## Requirements:

- [Python 2.7](https://www.python.org/download/releases/2.7/) (Other versions may work fine, but are untested by me)
- [BeautifulSoup 4.4.1](http://www.crummy.com/software/BeautifulSoup/) (Other versions may work fine, but are untested by me)
-`messages.htm` file (html\messages.htm) from your [Facebook archive](https://www.facebook.com/help/212802592074644).

## How to run:

1. Make sure [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) is installed.
2. Place your `messages.htm` file in the same directory as the `parser.py` file.
3. From the command line in that directory run `python parser.py messages.htm`
4. The script will now create (or re-create if run again) a `messages_reversed.html` file in the same directory containing your reversed messages.
5. After a while, depending on the size of your messages, the command line will output the message `done` when it has completed. Now your messages should be reversed.

### Things to note about the Facebook archive:

- Conversations from Facebook in the archive are currently split up into threads.
- These threads are limited to 20,000 messages before they are split up into other threads. 
- The downloaded archive does not guarantee that these threads (or groups of messages with an individual) are in the correct order and they could be divided by other conversations.
- Facebook message archives do not currently show emoticons.

### Things to note about the script:

- Any Unicode characters in the Facebook message archive will be re-encoded  (and possibly removed) as UTF-8.
- While the HTML file is no longer directly linked to the CSS sheet, the HTML tags were left alone if one wanted to introduce a style to it later. (I did this to make it easier to copy the messages from this archive into a document).
- This is a bare-bones script whose primary purpose is to solely reverse large quantities of messages. It is not meant to re-create the archive file. 
- Depending on how many messages you have, this may take a while to run. My Facebook message archive was around 20 MB in size. This took 5-10 minutes to complete on my desktop.
- Every time the script runs it will remove and re-create the messages_reversed.html.