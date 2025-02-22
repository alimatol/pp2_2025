import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

interfaces = [entry["l1PhysIf"]["attributes"] for entry in data["imdata"]]

print("Interfaces Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

for item in interfaces:
    print(f"{item['dn']:<50} {item['descr']:<20} {item['speed']:<10} {item['mtu']:<10}")
