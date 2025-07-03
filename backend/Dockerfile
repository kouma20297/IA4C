FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# RUN apt-get update && apt-get install -y \
#     gcc \
#     libmariadb-dev \
#     default-libmysqlclient-dev \
#     pkg-config \
#     python3-dev \
#     && pip install --upgrade pip \
#     && pip install -r requirements.txt \
#     && apt-get clean

# RUN apt-get update && apt-get install -y \
#     git \
#     gcc \
#     libmariadb-dev \
#     default-libmysqlclient-dev \
#     pkg-config \
#     python3-dev \
#     && pip install --upgrade pip \
#     && pip install -r requirements.txt \
#     && pip install pytest pytest-django \
#     && apt-get clean
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libmariadb-dev \
    default-libmysqlclient-dev \
    pkg-config \
    python3-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pytest pytest-django Pillow \
    && apt-get clean


COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["sleep", "infinity"]


