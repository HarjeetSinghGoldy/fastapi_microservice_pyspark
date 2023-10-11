FROM ubuntu:18.04
RUN apt-get update && apt-get -y update
RUN apt-get -y update \
    && apt-get install -y wget \
    && apt-get install -y jq \
    && apt-get install -y lsb-release \
    && apt-get install -y openjdk-8-jdk-headless \
    && apt-get install -y build-essential python3-pip \
    && pip3 -q install pip --upgrade \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
            /usr/share/man /usr/share/doc /usr/share/doc-base

ENV PYSPARK_DRIVER_PYTHON=python3
ENV PYSPARK_PYTHON=python3
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
# Set environment variables
# ENV APP_HOST=0.0.0.0
# ENV APP_PORT=8000

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port on which your FastAPI app will run
EXPOSE ${APP_PORT}

# Start your FastAPI app
CMD ["sh", "-c", "uvicorn main:app --host ${APP_HOST} --port ${APP_PORT} --reload"]
