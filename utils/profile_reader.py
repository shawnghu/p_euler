'''
cProfile reader.
'''

import argparse
import pstats
import pdb

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('filename')
    arg_parser.add_argument('--mode', default='print_top')
    args = arg_parser.parse_args()

    p = pstats.Stats(args.filename)
    p.sort_stats('cumulative')
    if args.mode == 'print_top':
        p.print_stats(10)
    elif args.mode == 'explore':
        pdb.set_trace()

if __name__ == '__main__':
    main()
