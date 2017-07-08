from pprint import pprint
import md2py

# Get content of the markdown file
markdown = open("exampleissue.md", "r")
content = markdown.read()
toc = md2py.md2py(content)

#Empty list for now
sections = []

# Print each heading
for heading in toc:
    # Some things have a newlines as well, split those too
    individualLines = str(heading).splitlines()
    for line in individualLines:
        print(line)
        print('             ')
        if "title: Issue" in str(line):
            title = line
            print('  TITLE   - ' + str(title))
        elif len(str(line)) < 20:
            if "layout: post" not in line:
                sections.append(line)
        else:
            print('Section seems to be a line of text')

print('')
print('===================================================')
print('OVERVIEW BELOW')
print('===================================================')
print('  TITLE   - ' + str(title))
for section in sections:
    print('  SECTION - ' + str(section))
#Prints the contents read in
#pprint(vars(toc))