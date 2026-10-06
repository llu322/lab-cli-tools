from zipfile import ZipFile, BadZipFile
import zlib

with open("Ashley-Madison.txt") as file:
    passwords = []
    for line in file:
        passwords.append(line.strip())

with ZipFile("whitehouse_secrets.zip") as zf:
    for count, password in enumerate(passwords, start=1):
        if count % 10000 == 0:
            print("Trying:", count, password)
        try:
            zf.extractall(pwd=password.encode())
        except (RuntimeError, BadZipFile, zlib.error):
            continue
        print("Password found:", password)
        break