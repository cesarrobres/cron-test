import json
from datetime import datetime

data = {
    "mensaje": "Ejecución automática",
    "fecha": datetime.utcnow().isoformat()
}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON creado correctamente")