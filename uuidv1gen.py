import optparse
import datetime
import sys
from classes.uuid import UUIDV1

def menu():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--uuid', dest="uuids", help='Comma separated uuids')
   
    options, args = parser.parse_args()
    globals().update(locals())

def order_uuids(uuid_one: str, uuid_two: str):
    high = uuid_one
    low = uuid_two

    if uuid_two >= uuid_one:
        high = uuid_two
        low = uuid_one

    return high, low

def check_input(uuid_input: str):
    if not uuid_input:
        sys.exit("UUIDs not found, use -u to pass uuids")

    if "," not in uuid_input:
        sys.exit("UUIDs must be comma separated, ex: uuid1,uuid2")

menu()

check_input(options.uuids)

extracted_values = options.uuids.split(",")

first_uuid = UUIDV1(extracted_values[0])
second_uuid = UUIDV1(extracted_values[1])

first_uuid.validate_input()
second_uuid.validate_input()

first_uuid.extract_chunks()
second_uuid.extract_chunks()

first_dec = first_uuid.get_decimal_representation() 
second_dec = second_uuid.get_decimal_representation()

high, low = order_uuids(first_dec, second_dec)

total_possibilities = high-low

print("There are a total of", total_possibilities, "possibilities")
decision = input("Would you like to continue? y/n" + "\n")
if decision == "n":
    sys.exit()

print(f'Generating {total_possibilities} UUIDs...')
with open('generated_uuids.txt', 'a') as out:
    while low <= high:
        low = low + 1
        hexa_value = hex(int(low))[2:]
        out.write(f'{hexa_value[:8]}-{hexa_value[8:12]}-{first_uuid.chunks[2]}-{first_uuid.chunks[3]}-{first_uuid.chunks[4]}' + '\n')
