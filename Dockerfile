FROM python:3.6.0
RUN mkdir scraper
RUN mkdir data
WORKDIR /scraper
COPY bscnn3.py jobs.cron jobs.log ./
RUN pip install beautifulsoup4
RUN pip install lxml
RUN apt-get update
RUN apt-get --yes install cron
RUN crontab jobs.cron
CMD ["cron", "&&", "tail", "-f", "jobs.log"]
