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
paragraphs = [[]]
offset = 0

for i in range(len(content)):
    if content[i] == "\n":
        paragraphs.append([])
        offset += 1
    else:
        paragraphs[offset].append(content[i])

# add a title for the body of the document
title_suggestion = paragraphs[0][0]

# indicates whether or not the title is in the contents(if so it does not write the title as a paragraph): 0 = False, 1 = True
title_included = 0

print(
    f'Enter a title for your document(enter "@f" to make "{title_suggestion}" the title): ')
doc_title = input()
if doc_title == "@f":
    doc_title = title_suggestion
    title_included = 1
title = body.h1
title.string = doc_title

# add the paragraph to the website
for par in range(title_included, len(paragraphs)):
    new_paragraph = doc.new_tag("p")
    body.append(new_paragraph)

    for line in paragraphs[par]:
        new_paragraph.append(line)
        new_row = doc.new_tag("br")
        new_paragraph.append(new_row)

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
