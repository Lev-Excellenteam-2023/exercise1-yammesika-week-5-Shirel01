
# import shutil

def read_file_bytes(file):
    with open(file, 'rb')as jpg:
        f = jpg.read()
        print(f)
import string

def read_file(file):
    with open(file, 'rb') as jpg:

        while True:
            line = file.readline()
            if line:
                for data in line:
                    if data
            else:
                break
        content = jpg.read()
        for data in content:
            while data.
        # data = content.endswith(?).decode()

        # print(data)

read_file_bytes('logo.jpg')


def read_file_in_chunks(file_object, chunk_size=3072):
    while True:
        # Just read chunk_size size data.
        data = file_object.read(chunk_size)
        # If it reach to the end of the file.
        if not data:
            # Break the loop.
            break
        yield data


# Open the big log data file.
with open('logo.jpg') as f:
    # Invoke the above lazy file read data function.
    for piece in read_file_in_chunks(f):
        # Process the piece of data such as write the data to another file.
        process_data(piece)
503