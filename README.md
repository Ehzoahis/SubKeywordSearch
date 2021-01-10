# Subject Keywords Search
Search sentences from abstracts of articles in ArXiv dataset base if the keyword matches the subject of the sentence. Highlight the subjects containing the keywords.

Made my Haozhe Si, 01/10/2021

## Dataset
[Cornell ArXiv Dataset](https://www.kaggle.com/Cornell-University/arxiv)

## Package Usage
### SpaCy
Use SpaCy model to perform denpendency parsing. Don't have to install if not modifying ```myindex```. The model is not 100% accurate and may cause some issues in searching. 
```python
pip install spacy
python -m spacy download en_core_web_sm
```
### Whoosh
Use Whoosh module to build the searching engine.
```python
pip install whoosh
```
### Flask
Use Flask module to build the web interface. The module will open a local host at http://127.0.0.1:5000/.
```python
pip install flask
```
## Usage
Download ```core.zip```, unpack and run
```python
python arxiv_web.py
```

By default, the corpus size is 10,000. Can modify the size of corpus in ```archivesearch.ipynb```.
