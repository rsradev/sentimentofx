FROM python:3.13-slim

RUN curl -Ls https://astral.sh/uv/install.sh | bash

RUN ~/.cargo/bin/uv pip install -r pyproject.toml

COPY ./sentimentofx ./sentimentofx

CMD ["uvicorn", "sentimentofx.main:app", "--host", "0.0.0.0", "--port", "8000"]