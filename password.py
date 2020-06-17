import argparse
import secrets
import string


def generate_password(char: int, symbol: int):
    words = string.ascii_letters+string.digits
    if symbol:
        words += "!#$%&()*+,-.:;<=>?@[]^_`{|}~"
    return "".join(secrets.choice(words) for _ in range(char))


def setup_parser():
    parser_ = argparse.ArgumentParser(description="Script for generate password")
    parser_.add_argument(
        "-l",
        "--length",
        help="specify the length of password, 密码的长度",
        type=int,
        default=16,
        dest="length",
    )
    parser_.add_argument(
        "-s",
        "--symbol",
        help="specify if the password need symbol, 0 for no, 1 for yes, 密码是否有符号",
        type=int,
        default=0,
        dest="symbol",
    )
    parser_.add_argument(
        "-r",
        "--repeat",
        help="specify how many password you need, 生成密码的个数",
        type=int,
        default=1,
        dest="repeat",
    )
    return parser_


if __name__ == '__main__':
    parser = setup_parser()
    _args = parser.parse_args()
    for _ in range(_args.repeat):
        print()
        print(" "*5, generate_password(_args.length, _args.symbol))
        print()
