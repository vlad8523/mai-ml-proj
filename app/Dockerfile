FROM python:3.10
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
RUN python -m nltk.downloader stopwords
COPY ./ /code/
ENTRYPOINT ["python", "main.py"]