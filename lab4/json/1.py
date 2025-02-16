import json

with open("json/json_test.json", "r") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 87)
print(f"{'DN':<50} {'Description':<20} {'speed':<10} {'MTU':<10}")
print("-" * 49,"", "-" * 19,"","-" * 6,"", "-" * 8)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {'':<20} {speed:<10} {mtu:<10}")