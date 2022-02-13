# syntax=docker/dockerfile:1
FROM python
RUN echo 'we are running some # of cool things'
COPY ./src /src
COPY ./ssl /ssl
COPY ./data /data
CMD python /src/main.py