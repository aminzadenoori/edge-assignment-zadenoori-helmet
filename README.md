
# Koone edge-assignment-temp

<div align="center">
    <img src="https://www.binoocle.com/wp-content/uploads/2019/10/Risorsa-1@2x-1.png" alt="Logo">
    <h3 align="center">Koone edge assignment template </h3>
    <p align="center">
    a template repository for edge processing on foss softwares and devices 
        <br />
        <a href="https://github.com/bino-ocle/edge-assignment-temp/issues">Report Bug/Request Feature</a>
    </p>
</div>

This repository contains a reusable temoplate for pi4-edge-processing device.

### Prerequisites

- `poetry` env manager
- `docker`
- raspberry pi-4 


<p align="right">(<a href="#top">back to top</a>)</p>

### Architecture

The project architecture follows the structure below:

- **app/config**: this directory stores the project configuration files:
  - **.env**: contains environment variables
  - **logging.ini**: contains logger configuration
  - **environment.py**: contains pydantic environment model 

- **tests**: contains the pytest tests

- **app/utils**: contains reusable utils functions:
  - **logger.py**: contains the logger instance 

- **app/main.py**: contains the debugging workflow
- **app/cv_camera.py**: contains initialization fro CVCamera object class

the tree structurw looks like:

```bash
.
├── app
│  ├── __init__.py
│  ├── client.py
│  ├── config
│  │  ├── __init__.py
│  │  ├── environment.py
│  │  └── logging.ini
│  ├── constants.py
│  ├── cv_camera.py
│  ├── data
│  │  └── placeholder.md
│  ├── main.py
│  ├── ssd
│  │  ├── __init__.py
│  │  ├── detect.py
│  │  ├── detector.py
│  │  ├── ssd_mobilenet_v2_coco_quant_postprocess.tflite
│  │  └── utils.py
│  └── utils
│     ├── __init__.py
│     ├── logger.py
│     └── slack_messages.py
├── Dockerfile.template
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.cfg
├── start.sh
├── tests
│  ├── __init__.py
│  └── test_model.py
└── update_balena.bat
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Getting Started

Create a new virtual environment by running the command below with you preferred tool, I use `poetry`:

```sh
poetry install
poetry shell
```

Otherwise wiht venv:

```sh
python -m venv .venv
```

Activate it in a Linux enviroment by running:

```sh
source .venv/bin/activate
```

or in a Windows enviroment by running:

```sh
.\.venv\Scripts\activate
```

Install the dependencies by running:

```sh
pip install -r requirements.txt
```

Create a new environment file `.env` e.g. just like the on in `app/config/env.sample` inside `app/config` dir in which you need to store env variables.
Please [ping me](mailto:n.salvini@binoocle.com) to have SLACK_TOKEN 

```sh
    DEVICE_ID=12345
    AUTH_KEY='mnbvcxzlkjhgfdsapoiuytrewq'
    RESIZE=300,300
    SCORE_TH=0.5
    SHOT_DELAY=2
    CAMERA_INIT_DELAY=10
    SLACK_TOKEN='qwertyuiopasdfghjklzxcvbnm'
    SLACK_ERROR_LINK="https://github.com/bino-ocle/<your repo>"
    SLACK_ERROR_LINK_NAME="<your repo>"
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Run Tests

Before running forecasts locally, run test cases:

```sh
pytest ./tests/
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Deploy on Docker + Balena


<p align="right">(<a href="#top">back to top</a>)</p>

### Contact

Niccolò Salvini - [n.salvini@binoocle.com](mailto:n.salvini@binoocle.com)


<p align="right">(<a href="#top">back to top</a>)</p>