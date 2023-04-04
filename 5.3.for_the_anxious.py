
def read_file_bytes(file):
    with open(file, 'rb')as jpg:
        f = jpg.read()
        s = str(f)
        message = ""

        for string in s:
            if len(message) >= 5:
                if string == '!':
                    yield message
                    message = ""

                else:
                    if string.islower():
                        message += string

                    else:
                        message = ""

            else:
                if string.islower():
                    message += string

                else:
                    message = ""


def main():
    d = read_file_bytes('logo.jpg')
    for item in d:
        print(item)


if __name__ == "__main__":
    main()





