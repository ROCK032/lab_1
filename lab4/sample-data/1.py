import json

with open("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<55} {'Description':<20} {'Speed':<10}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "N/A")
    print(f"{dn:<55} {description:<20} {speed:<10}")
