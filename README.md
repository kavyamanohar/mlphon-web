

# Web interface for mlphon: Malayalam Phonetic Analyser and Generator

Flask based web interface for Malayalam Phonetic analyser and generator


Installation
------------

Create a virtual environment. In linux based systems, it is like this:
```
python -m venv ENV_DIR
source ENV_DIR/bin/activate
```

Then install the dependencies

```
pip install -r requirements.txt
```


Start the webserver and open the URL given in the output with a web browser.

```
gunicorn --bind :8000 --workers 1 --threads 8 mlphonweb:app
```

And open browser at localhost:8000
 
