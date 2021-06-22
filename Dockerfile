FROM alpine:latest

WORKDIR /opt
# install gnuradio dependencies
RUN apk update && apk add gnuradio --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/

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