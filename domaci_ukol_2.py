#zadani: https://github.com/AnetaPopelova/czechitas-programovani-v-pythonu-2024-03/blob/main/ukoly/02-obchodni-rejstrik.md

""" # cast 1
import requests

ico = input("Vlož číslo objektu: ")
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
#print(response)

data = response.json()
obchodni_jmeno = data.get("obchodniJmeno", {})
sidlo = data.get("sidlo", {}).get("textovaAdresa")

print(obchodni_jmeno,
      sidlo)
 """
# cast 2
import requests
import json

nazev_subjektu = input("Vlož název subjektu: ")

path = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
headers = headers={
    "accept": "application/json",
    "Content-Type": "application/json",
    }
data = json.dumps({"obchodniJmeno": nazev_subjektu})

response = requests.post(path, headers = headers, data = data)
#print(response)

new_data = response.json()

celkovy_pocet = new_data.get("pocetCelkem", 0)

subjekty = new_data.get("ekonomickeSubjekty", [])

print(f"Nalezeno subjektů: {celkovy_pocet}")

for subjekt in subjekty:
    obchodni_jmeno = subjekt.get("obchodniJmeno", [])
    ico = subjekt.get("ico", [])
    print(f"{obchodni_jmeno}, {ico}")