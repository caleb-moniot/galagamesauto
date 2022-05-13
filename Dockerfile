ARG PYTHON_VERSION=3.8.1
FROM python:${PYTHON_VERSION}-slim-buster

COPY Pipfile* ./
COPY test*.py ./

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

ENV PATH="/root/.local/bin:${PATH}"

CMD ["pipenv", "run", "pytest", "test_gala_games.py", "-v", "--color=yes"]
