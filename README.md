# Symptom checker

## Installation

Clone this repo and install the dependencies:

```bash
git clone https://github.com/phamnam-mta/symptom-checker.git
cd symptom-checker
pip install -r requirements.txt
```

Train model by command

```bash
rasa train
```

Start rasa and action server with UI-Webchat

```bash
rasa run -m models --enable-api --cors "*" --debug
rasa run actions
```
Open file `index.html` on web browser to test Chatbot


Start rasa locally
```bash
rasa run actions
rasa shell
```
