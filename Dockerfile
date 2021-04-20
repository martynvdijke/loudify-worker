FROM ubuntu

WORKDIR /opt
# install gnuradio dependencies
RUN apt-get -yqq update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get -yqq install gnuradio cmake swig git liborc-0.4-dev python3-venv python3 python3-pip wget iputils-ping

# install gnuradio OOT LoRa (gr-lora_sdr)
RUN git clone --depth 1 https://github.com/martynvdijke/gr-lora_sdr.git /opt/gr-lora_sdr && cd gr-lora_sdr && mkdir -p build && cd build && cmake ../ && make install

# copy all the files to the container
ADD . /opt/loudify-worker
# set a directory for the app
WORKDIR /opt/loudify-worker
# install python dependencies
RUN pip3 install -r requirements.txt


# tell the port number the container should expose
EXPOSE 5000

# run the command
# CMD ["python", "./app.py"]
# CMD . /opt/venv/bin/activate && exec python myapp.py