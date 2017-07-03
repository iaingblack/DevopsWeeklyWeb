import io
import pypandoc
import panflute

def action(elem, doc):
    if isinstance(elem, panflute.Image):
        doc.images.append(elem)
    elif isinstance(elem, panflute.Link):
        doc.links.append(elem)

if __name__ == '__main__':
    data = pypandoc.convert_file('example.md', 'json')
    doc = panflute.load(io.StringIO(data))
    doc.images = []
    doc.links = []
    doc = panflute.run_filter(action, prepare=prepare, doc=doc)

    print("\nList of image URLs:")
    for image in doc.images:
        print(image.url)
