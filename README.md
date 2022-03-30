# Symptom checker

## Installation

Clone this repo and install the dependencies:

```bash
git clone https://github.com/phamnam-mta/symptom-checker.git
cd symptom-checker
pip install -r requirements.txt
```

## Setup Neo4j for RS
```bash
sudo systemctl start neo4j.service
export NEO4J_URL=http://localhost:7474/
export NEO4J_AUTH=neo4j/password
```

## Train model by command

```bash
rasa train
```

## Start rasa and action server with UI-Webchat

```bash
rasa run -m models --enable-api --cors "*" --debug
rasa run actions
```
Open file `index.html` on web browser to test Chatbot


## Start rasa locally
```bash
rasa run actions
rasa shell
```

## Deploy with ngrok
```bash
rasa run actions
rasa run -m models --enable-api --cors "*" --debug
ngrok http 5005
```

## Use recommend carousel
Put the action behind the ending response. Example:
```
stories:
- story:
  steps:
  - intent: affirm
  - action: utter_high_fever_urgent_out
  - action_recommend_doctors
```