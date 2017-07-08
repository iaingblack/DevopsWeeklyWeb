import io
import md2py

# Get content of the markdown file
markdown = open("exampleissue.md", "r")
content = markdown.read()

toc = md2py.md2py(content)
for item in toc:
    print(item)


#>>> toc.h1
#Chikin Tales
#>>> str(toc.h1)
#'Chikin Tales'
