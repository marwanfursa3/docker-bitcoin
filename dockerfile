FROM python

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ma.py .

CMD ["python","ma.py"]                     
