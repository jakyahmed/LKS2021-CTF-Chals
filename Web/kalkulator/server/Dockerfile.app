FROM python:3

RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN echo "LKS2021{dikala_kalkulatorku_bertindak_disitulah_servermu_meledak}" > /flag

USER www

EXPOSE 5000
CMD ["python", "main.py"]
