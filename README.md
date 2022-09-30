# pandas_meetup

![Meetup Photo](img/eats_shoots_and_leaves.png)

## Summary
Pandas 101 with a smattering of DevOps and TUI

**Table of Contents**
* [pandas_meetup](#pandas_meetup)
  * [Summary](#summary)
  * [Setup](#setup)
  * [Usage](#usage)
    * [Poetry](#poetry)
    * [Docker](#docker)
    * [Both](#both)
  * [TODO](#todo)
  * [Further Reading](#further-reading)

## Setup
* Install
    * [editorconfig](https://editorconfig.org/)
    * [asdf](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf)
    * [poetry](https://python-poetry.org/docs/)
    * [docker](https://docs.docker.com/compose/install/)
    * [just](https://just.systems/man/en)

## Usage
### Poetry
* Install requirements via Poetry: 
    ```bash
    poetry install
    poetry run ipython kernel install --name "python3.10.7" --user
    ```
* Run Jupyter Lab
    ```bash
    poetry shell
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
    ```
* Quit the server via `ctrl-c` in the terminal
* Enter `deactivate` to exit the Poetry virtual environment

### Docker
* Customize the `.env.example` and rename to `.env`
* General commands
    ```bash
    # build image locally
    docker-compose build --pull --no-cache

    # start container
    docker-compose up -d

    # stop container
    docker-compose stop

    # remove container and network
    docker-compose down
    ```
* `justfile` syntax (recommended)
    ```bash
    # help
    just

    # build image locally (no-cache)
    just build-clean

    # build image locally
    just build

    # start container
    just start

    # ssh
    just exec

    # stop container
    just stop

    # stop container, remove container and network
    just down
    ```

### Both
* Open a browser and navigate to `http://127.0.0.1:8888`
  * Docker uses the token specified in `.env`
* Select the `python3.10.7` kernel if asked
* Open `demo_pandas.ipynb` from the left-hand column
* Run cells by selecting them and pressing `shift-enter`

## TODO
* Polish. Probably.
* Fix *bonus* code (audience participation??)

## Further Reading
[Original Repo](https://github.com/realpython/materials/tree/master/pandas-intro)

[Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)

[Dockerizing Jupyter Projects](https://towardsdatascience.com/dockerizing-jupyter-projects-39aad547484a)

[The Spotify Hit Predictor Dataset (1960-2019)](https://www.kaggle.com/datasets/theoverman/the-spotify-hit-predictor-dataset)

[Jupyter Docker Stacks — Docker Stacks documentation](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)

[Using Pandas and Python to Explore Your Dataset – Real Python](https://realpython.com/pandas-python-explore-dataset/)

[pandas GroupBy: Your Guide to Grouping Data in Python – Real Python](https://realpython.com/pandas-groupby/)

[SQL Versions of the Most Frequently Used Pandas Functions | Towards Data Science](https://towardsdatascience.com/sql-versions-of-the-most-frequently-used-pandas-functions-bb6399f87461)
