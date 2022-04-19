import argparse

def cml():
    parser = argparse.ArgumentParser(description='Readable to Leet Converter')
    parser.add_argument('-self', dest='type', type=str, default=max,
                        help='initiates Self Bot')

    parser.add_argument(None, default=max,
                help='Default: Regular Manual Command Line Leet Converter')

    args = parser.parse_args()
