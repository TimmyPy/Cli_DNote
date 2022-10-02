from argparse import ArgumentParser

parser = ArgumentParser(description='CLI Tool to create one day notes')
subparsers = parser.add_subparsers(help='Sub-command help')

parser_create = subparsers.add_parser('create', help='Create action help')
parser_create.add_argument('note', help='Note body')

parser_read = subparsers.add_parser('read', help='Read action help')
parser_read.add_argument('-l', help='List of notes')
parser_read.add_argument('-a', help='All information about note')

parser_update = subparsers.add_parser('update', help='Update action help')
parser_update.add_argument('--id', type=int, help='Uniq identifier of a note')

parser_delete = subparsers.add_parser('delete', help='Delete action help')
parser_delete.add_argument('--id', type=int, help='Uniq identifier of a note')
