# Healthcare Professional Recommendation System

### Quick Started
1. Installation
```bash
pip install -r requirements.txt

git clone https://VinBrain@dev.azure.com/VinBrain/AI%20-%20NLP%20Management/_git/recommender_system
```
2. Start Neo4j service
```bash
sudo systemctl start neo4j.service
```

3. Export path
```bash
export NEO4J_URL=http://localhost:7474/
export NEO4J_AUTH=[your_user]/[your_password]
```

4. Run query code
```bash
from rs import Recommender

NEO4J_URL = os.getenv("NEO4J_URL", None)
NEO4J_AUTH = os.getenv("NEO4J_AUTH", None)
user = NEO4J_AUTH.split("/")[0]
password = NEO4J_AUTH.split("/")[1]
recommender = Recommender(NEO4J_URL, user, password)


if __name__ == '__main__':
    request = {
        'symptom': "sốt",
        'speciality': '',
        'age': '30'
    }
    doctors = recommender.suggest_doctors(request) # List[Dict]
```