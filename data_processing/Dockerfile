FROM ubuntu:22.04

RUN apt-get update 

RUN apt-get -y install cron

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

WORKDIR /app

COPY . /app

RUN python3 -m pip install -r requirements.txt

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/data_processing_cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/data_processing_cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Apply cron job
RUN crontab /etc/cron.d/data_processing_cron

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log