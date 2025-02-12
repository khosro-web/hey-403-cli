import argparse

from src.cli.help_formater import CustomHelpFormatter


def create_base_parser():
    return argparse.ArgumentParser(
        description="Hey 404 DNS Analyzer",
        add_help=False,
        formatter_class=CustomHelpFormatter,
    )


def add_common_arguments(parser):
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message",
    )

    parser.add_argument(
        "url", type=str, help="Target URL/domain to test (e.g., example.com)"
    )
    return parser


def build_parser():
    parser = create_base_parser()
    parser = add_common_arguments(parser)
    return parser
