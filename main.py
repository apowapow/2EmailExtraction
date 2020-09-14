import re
from pprint import pprint

FILE_SAMPLE = "sample.txt"
READ_ONLY = "r"


def main():
    addr = {}

    with open(FILE_SAMPLE, READ_ONLY) as f:
        file_content = f.read().replace('\n', ' ').split(' ')

    for fc in file_content:
        result = re.findall("^[a-zA-Z0-9.'_%+-]+[@]{1}[a-zA-Z0-9.'_%+-]+$", fc)

        if len(result) > 0:
            fc_partition = fc.partition("@")
            local = fc_partition[0]
            domain = fc_partition[2]

            if domain not in addr:
                addr[domain] = []

            addr[domain].append(local)

    addr_freq = sorted([(domain, len(local)) for domain, local in addr.items()], key=lambda t: t[1], reverse=True)
    pprint(addr_freq)


if __name__ == "__main__":
    main()
