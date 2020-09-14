import re

FILE_SAMPLE = "sample.txt"
READ_ONLY = "r"


def main():
    d = {}

    with open(FILE_SAMPLE, READ_ONLY) as f:
        file_content = f.read().replace('\n', ' ').split(' ')

    for fc in file_content:
        result = re.findall("^[a-zA-Z0-9.'_%+-]+[@]{1}[a-zA-Z0-9.'_%+-]+$", fc)

        if len(result) > 0:
            fc_partition = fc.partition("@")
            local = fc_partition[0]
            domain = fc_partition[2]

            if domain not in d.keys():
                d[domain] = []

            d[domain].append(local)

    for domain, local in d.items():
        print("{0}: {1}".format(domain, len(local)))


if __name__ == "__main__":
    main()
