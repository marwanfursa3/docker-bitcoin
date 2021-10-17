FROM python

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY bitcoin.py .

CMD ["python","bitcoin.py"]                     