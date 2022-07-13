from bs4 import BeautifulSoup

# get the website content
print("Enter file directory")
dir_ = input()
if dir_ == "t":
    dir_ = "content.txt"
with open(dir_, "r") as f:
    content = f.readlines()

with open("shell.html", "r") as shell:
    doc = BeautifulSoup(shell, "html.parser")
    body = doc.body
    head = doc.head

# divides the text into paragraphs
paragraphs = []
paragraph = []
for i in range(len(content)):
    if content[i] == "\n":
        paragraphs.append(paragraph)
        paragraph.clear()
    else:
        paragraph.append(content[i])
if content[len(content) - 1] != "\n":
    paragraphs.append(paragraph)

# add the paragraph to the website
for par in paragraphs:
    new_paragraph = doc.new_tag("p")
    body.append(new_paragraph)

    for line in par:
        new_paragraph.append(line)
        new_row = doc.new_tag("br")
        new_paragraph.append(new_row)

print("Enter a title for your document: ")
doc_title = input()
title = body.h1
title.string = doc_title

print("Enter a title for your website: ")
site_title = input()
title = head.title
title.string = site_title


# put the code for the new website in its file
with open("website.html", "w") as website:
    website.truncate(0)
    website.seek(0)
    website.write(str(doc))

print("Website Complete!")
