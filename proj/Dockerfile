FROM python:3.13.9
WORKDIR /proj
COPY req.txt .
RUN pip install -r req.txt
COPY main.py .
CMD ["uvicorn","proj.main:proj"]
