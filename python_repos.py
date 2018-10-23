import requests

# Führt einen API-Aufruf durch und speichert die Antwort.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Speichert die API-Antwort in einer Variablen.
response_dict = r.json()

# Verarbeitet die Ergebnisse.
print(response_dict.keys())