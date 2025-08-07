import uuid

# based on current time and mac-address
id1 = uuid.uuid1()
print(id)

# based on pseudo-random numbers
id2 = uuid.uuid4()
print(id1)

# based on hashing a namespace identifier
# and a string using the MD5 algorithm
id3 = uuid.uuid3(uuid.NAMESPACE_OID, 'iphone')
print(id3)

# based on hashing a namespace identifier
# and a string using the SHA-1 algorithm
id4 = uuid.uuid5(uuid.NAMESPACE_OID, 'tv')
print(id4)

items = [['MacBook', 2000], ['Motherboard', 1100], ['SSD', 400], ['Ipad', 900]]
items_data = {}

for item in items:
    id = uuid.uuid5(uuid.NAMESPACE_OID, item[0])
    key = id.hex[:10]
    items_data[key] = item

print("Items Data:")
for key, value in items_data.items():
    print(f"{key}: {value}")
