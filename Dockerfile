FROM nvcr.io/nvidia/cuda:11.3.0-cudnn8-runtime-ubuntu20.04

RUN apt update && \
    apt install python3-pip -y

RUN pip3 install fvcore iopath
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
RUN pip3 install --no-index --no-cache-dir pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py38_cu113_pyt1110/download.html
