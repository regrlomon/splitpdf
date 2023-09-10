from langchain.document_loaders import PDFMinerPDFasHTMLLoader


loader = PDFMinerPDFasHTMLLoader('table.pdf')


doc = loader.load()
with open('test.html', 'w', encoding='utf-8') as file:
    file.write(doc[0].page_content)

