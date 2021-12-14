import csv
import os
from random import choices
from generators import top100_picker, top100k_picker, random_generator, humanlike_generator
from hashers import hash_md5, hash_sha1_salt, hash_bcrypt


def printProgressBar (iteration, total, prefix, suffix, decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()


def create_generator_picker(generators_with_weights):
    generators = [x for x, _ in generators_with_weights]
    weights = [x for _, x in generators_with_weights]
    return lambda: choices(generators, weights, k=1)[0]


def generate_passwords(n, generator_picker):
    return [generator_picker()() for _ in range(n)]


def to_file(filename, array):
    with open(filename, "w") as f:
        for x in array:
            f.write(str(x) + "\n")


def hashes_to_file(filename, hashes):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=hashes[0].keys())
        writer.writeheader()
        for x in hashes:
            writer.writerow(x)


if __name__ == "__main__":
    target_directory = "generated"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    generators_with_weights = (
        (top100_picker, 10),
        (top100k_picker, 65),
        (random_generator, 5),
        (humanlike_generator, 20)
    )
    generator_picker = create_generator_picker(generators_with_weights)

    print("Started password generation")
    passwords = generate_passwords(100000, generator_picker)
    to_file(os.path.join(target_directory, "passwords.txt"), passwords)

    print("Started md5 generation")
    md5 = [hash_md5(x) for x in passwords]
    to_file(os.path.join(target_directory, "md5.txt"), md5)

    print("Started sha1_salt generation")
    sha1_salt = [hash_sha1_salt(x) for x in passwords]
    to_file(os.path.join(target_directory, "sha1_salt.txt"), sha1_salt)

    print("Started bcrypt generation")
    bcrypt = [hash_bcrypt(x) for x in passwords]
    to_file(os.path.join(target_directory, "bcrypt.txt"), bcrypt)