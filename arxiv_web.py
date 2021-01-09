from flask import Flask, request, render_template
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import webbrowser

ix = open_dir("myindex")

def searchArxiv(key_words, ix=ix):
    resultList = []
    with ix.searcher() as searcher:
        parser = QueryParser("subj", ix.schema)
        query = parser.parse(key_words)
        results = searcher.search(query, limit=None)
        if len(results) != 0:
            for result in results:
                resultList.append(result['content'])
        return resultList
    
app = Flask("APP")

@app.route('/')
def main_page():
    return render_template('arvix_search.html')

@app.route('/', methods=['POST'])
def main_page_post():
    kw = request.form['keyword']
    resultList = searchArxiv(kw)
    if len(resultList) == 0:
        output = "No Matched Result."
    else:
        resultList.append("<br>{} Matched".format(len(resultList)))
        output = "<br><br>".join(resultList)
    return render_template('arvix_search.html',output=output)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")    
    app.run()