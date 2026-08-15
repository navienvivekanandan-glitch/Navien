#2025 A Level Paper 2
#Task 4

#Task 4.1
hashtable = []
for i in range(100):
  hashtable.append(None)
print(hashtable)

#Task 4.2

def calculate_hash(key_field):
    hash_value = key_field % 100
    return hash_value


#Task 4.3

def insert(key_field,string_data):
    hash_value = calculate_hash(key_field)
    count_not_free = 0
    while hashtable[hash_value] != None:
        hash_value = (hash_value +1) % 100
        count_not_free += 1
        if count_not_free >= 100:
            return False
            break
        
    hashtable[hash_value] = string_data

    return True


#Task 4.4

def read_data():
    file = open('records.txt','r')
    for line in file:
        line = line.strip()
        line = line.split(' ')
        key_field = int(line[0])
        string_data = line[1]
        result = insert(key_field,string_data)
        if result == False:
            print("The string_data ",key_field,string_data," is not appended to the hashtable")

    file.close()

print(read_data())
print(hashtable)


#Task 4.5

def find_record(key_field):
    hash_value = calculate_hash(key_field)
    value = hashtable[hash_value]

    if value == None:
        return False
    else:
        return value

print(find_record(557))

#Task 4.6

read_data()
result = find_record(475)

if result == False:
    print("Record not found")
else:
    print("This is the data_string associated with the key_filed: ", result)
    

    
