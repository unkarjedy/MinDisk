import argparse

def get_file_from_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed")
    args = parser.parse_args()
    s = open(args.filename)
    # s = sys.stdin
    return s
