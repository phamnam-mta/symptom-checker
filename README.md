# Symptom checker

## Installation

Clone this repo and install the dependencies:

```bash
git clone https://gitlab.com/phamnam.mta/sani.git
cd sani
pip install -r requirements.txt
```

Train model by command

```bash
rasa train
```

Start rasa and action server

```bash
rasa run -m models --enable-api --cors "*" --debug
rasa run actions
```
Open file `index.html` on web browser to test Chatbot