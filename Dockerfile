FROM python:3.9

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY main.py /
COPY base.html /
CMD ["python3", "./main.py"]
