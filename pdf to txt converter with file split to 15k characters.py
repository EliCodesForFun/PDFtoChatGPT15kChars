import fitz
import html
import os

#test
filepath = r"path\to\myfile.pdf"
filepath_output = os.path.splitext(filepath)[0]   #path\to\myfile

doc = fitz.open(filepath)  # open document
out = open(filepath_output + ".txt", "wb")  # open text output
filecount = 0
lencount = 0
for page in doc:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    out.write(text)  # write text of page
    lencount += len(text)
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)

out.close()


#Split up the text to 15,000 characters
with open(f"{filepath_output}.txt", "r", encoding="utf-8") as infile:
    text = infile.read()

#Changed to 14.5k due to chat-gpt limitations when we tack on our prompt
chunk_size = 14500
chat_gpt_prompt = """Summarize this book segment into key topics and explanations, and give an example of how to implement each topic with modern data engineering practices.
Use a format that looks like this:
"Key Topics:
•    Data maturity and its impact on data engineering
•    Data Engineering Skills and Activities across different stages of data maturity"
Explanation: "The book segment discusses the role of data engineers in modern data tooling landscape. It highlights the importance of creating agile data architectures and balancing cost-effective services that deliver value to the business..."
Here is the book segment:
"""

#makes a list of strings that are 14.5k characters long.
#iterator starts at 0. [i:i+chunk_size] is [0 to 15,000]. chunk_size is the increment in range, so it goes up by 15k.
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
print(chunks)

for i, chunk in enumerate(chunks):
    with open(f"filename_chunk_{i}.txt", "w", encoding="utf-8") as outfile:
        outfile.write(chat_gpt_prompt) #write the prompt to each file for quick copy-pasting
        outfile.write("\n") #line break in between
        print(type(chunk))
        #print(chunk)
        outfile.write(chunk)