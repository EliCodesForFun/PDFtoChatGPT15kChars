
# PDFtoChatGPT15kChars
This is a simple project you can use to turn your PDF into a .txt file, and then split it into 15k characters.

### Idea:
Chat-GPT has a limit of about 15k-16k characters of text when using it from the web.

### Problem:
I want to get a summary of a book that is over 1 million characters. I want to copy-paste segments of the book, along with my chat-gpt prompt each time, in order to get a summary of all the content in the book.

### Solution: 
This project will convert a file from pdf to txt, and split it up into 14.5k characters (under 15k due to potential long lines, and so that we can append our chat-gpt prompt to the beginning of each file.)


### Usage:

Install these first:
`pip uninstall fitz` # Do this because it can conflict with PyMuPDF

`pip install pymupdf -U` #might need to upgrade it
 

Change this:
`filepath = r"path\to\myfile.pdf"`

to an actual path such, like this:
filepath = r"C:\Users\Johny Bravo\The Greatest Workout Routine.pdf"

You can also change the `chat_gpt_prompt` variable, as I was using it to summarize a book on Data Engineering:


Run the .py file and and it will output a .txt file for the book, as well as chunks that are about 15,000 characters in length.
