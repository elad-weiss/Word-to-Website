from bs4 import BeautifulSoup

# get the website content
print("Enter file directory")
dir_ = input()
try:
    with open(dir_, "r") as f:
        content = f.readlines()
except:
    print("We had a problem with this file...")
    dir_ = "default.txt"
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

# add a title for the web page
print("Enter a title for your website: ")
site_title = input()
title = head.title
title.string = site_title

# choose a font and text alignment
print("Choose a font: ")
font_menu = {"0": "sans-serif", "1": "Helvetica", "2": "Arial", "3": "serif",
             "4": "Times", "5": "monospace", "6": "Courier New", "7": "Lucida Console"}
for i in range(0, len(font_menu), 2):
    print(str(i), font_menu[str(i)], "	  ", str(i+1), font_menu[str(i+1)])
print("Enter the number matching to your font: ")
font = input()
# check for bad input
if int(font) < 0 or int(font) > 7:
    font = "2"

print("choose the text alignment: ")
alignment_menu = {0: "left", 1: "center", 2: "right"}
for i in range(len(alignment_menu)):
    print(i, "=", alignment_menu[i])
text_alignment = input()
# check for bad input
if int(text_alignment) < 0 or int(text_alignment) > 2:
    text_alignment = 0

# set the styling
head.style.string = "body { font-family: " + \
    font_menu[str(int(font))] + ";\ntext-align: " + \
    alignment_menu[int(text_alignment)] + "; }"


# put the code for the new website in its file
with open("website.html", "w") as website:
    website.truncate(0)
    website.seek(0)
    website.write(str(doc))

print("Website Complete!")
print("It can be found inside this folder under the name 'website.html'")
