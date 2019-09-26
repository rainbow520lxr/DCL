import argparse

parser = argparse.ArgumentParser(description='dcl parameters')
parser.add_argument('--data', dest='dataset',
                    default='CUB', type=str)
parser.add_argument('--save', dest='resume',
                    default=None,
                    type=str)

args = parser.parse_args()

print(args)