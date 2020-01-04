FROM continuumio/miniconda3

# Install python packages
RUN mkdir /opt/api
COPY requirements.txt /opt/api/
RUN pip install -r /opt/api/requirements.txt

# Copy files into container
COPY swagger /opt/api/swagger
COPY model /opt/api/model
COPY steel_plate_fault_classification_api.py /opt/api/

# Set work directory and open the required port
WORKDIR /opt/api
EXPOSE 8080

# Run our service script
CMD ["python","steel_plate_fault_classification_api.py"]