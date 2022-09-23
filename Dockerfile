# build stage
FROM python:3.10 AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /project/
# COPY src/ /project/src

# install dependencies and project
WORKDIR /project
RUN pdm install --prod --no-lock --no-editable


# run stage
FROM python:3.10

# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/.venv/lib/python3.10/site-packages /project/pkgs

# set command/entrypoint, adapt to fit your needs
CMD ["python", "-m", "project"]