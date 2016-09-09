__author__ = 'sp41mer'
import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-r', type=str, help='Root directory of server')
    parser.add_argument('-c', type=int, help='CPUs quanity limit')
    args = parser.parse_args()
    ROOTDIR = vars(args)['r']
    NCPU = vars(args)['c']


if __name__ == '__main__':
    main()