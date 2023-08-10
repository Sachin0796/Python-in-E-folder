import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("Practisequestions/user.avsc", "rb").read())
schema2 = avro.schema.parse(open("Practisequestions/user2.avsc", "rb").read())
print("\n",schema,"\n")
writer = DataFileWriter(open("Practisequestions/users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("Practisequestions/users.avro", "rb"), DatumReader(schema,schema2) )
for user in reader:
    print(user)
reader.close()

ls=[i for i in range(0,20) if all(i%y for y in range(2,i//2)) ]
print(ls)