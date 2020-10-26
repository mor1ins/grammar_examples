import lark
import json
import pprint

from lark.exceptions import UnexpectedEOF, UnexpectedCharacters
from lark.reconstruct import Reconstructor
from transformers.parse_to_dict import ParseToDict
from transformers.black_list import BlackList
from transformers.get_full_number import GetFullNumber
from transformers.number_to_str import NumberToStr
from transformers.parse_country_codes import ParseCountryCodes
from transformers.remove_scopes import RemoveScopes


def read_grammar(filename):
    return ''.join(open(filename, 'r').readlines())


email_parser = lark.Lark(read_grammar('grammars/email_example.lark'))
phone_parser = lark.Lark(read_grammar('grammars/phone_example.lark'))

phone_to_json = (RemoveScopes()
                 * NumberToStr()
                 * GetFullNumber()
                 * ParseCountryCodes()
                 * ParseToDict())
email_to_json = (RemoveScopes()
                 * BlackList(['DOT', 'DOG'])
                 * ParseToDict())


def parse(parser, transformer, text):
    tree = parser.parse(text)
    dictionary = transformer.transform(tree)

    return tree, dictionary


def reconstruct(parser, tree):
    return Reconstructor(parser).reconstruct(tree)


def parse_and_reconstruct(parser, transformer, text):
    print(f'input: \t\t\t"{text}"')

    try:
        tree, dictionary = parse(parser, transformer, text)
        print(f'AST : \t\t\t{dictionary}')
        print(f'reconstructed: \t{reconstruct(parser, tree)}')
    except UnexpectedEOF:
        print('\tFinish, please...')
    except UnexpectedCharacters as err:
        out = '\t' + err.args[0].replace('\n\n', '\n').replace('\n', '\n\t')
        print(out)


if __name__ == "__main__":
    parse_and_reconstruct(phone_parser, phone_to_json, '+7 (942) 726-44-57')
    print()
    parse_and_reconstruct(phone_parser, phone_to_json, '+375 942 726 44 5')
    print()
    parse_and_reconstruct(email_parser, email_to_json, 'test.mail!@gmail.com')
    print()
    parse_and_reconstruct(email_parser, email_to_json, 'test.mail!@dwdw.')
    print()
    parse_and_reconstruct(email_parser, email_to_json, 'test.mail!@.com')
    print()
    parse_and_reconstruct(phone_parser, phone_to_json, '+375 942 726 44 51')

