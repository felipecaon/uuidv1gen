import sys

class UUIDV1:
    def __init__(self, value):
        self.value = value
        self.chunks = []

    def is_uuid(self):
        return "-" in self.value

    def is_uuid_v1(self):
        return self.value[14] == '1'

    def extract_chunks(self):
        self.chunks = self.value.split("-")

    def get_decimal_representation(self):
        first_chunk = self.chunks[0]
        second_chunk = self.chunks[1]
        hex_value = first_chunk + second_chunk
        return int(hex_value, 16)

    def validate_input(self):
        if not self.is_uuid():
            sys.exit(f'{self.value} is not an UUID')

        if not self.is_uuid_v1():
            sys.exit(f'{self.value} is not UUID v1')