import logging
import os
from tabulate import tabulate

import click as click

from dpsy_terminal_stats import config
from dpsy_terminal_stats.services import terminal_stats_service


def init_app():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


@click.command()
@click.option('-f', '--filename', type=str, required=True)
@click.option('--debug/--no-debug', default=None)
def cli(filename:str, debug: bool):
    # apply env variables first;
    # command line parameters have higher priority, so it goes after
    _apply_env_variables_to_config()

    if debug is not None:
        config.DEBUG_PRINT = debug

    stats = dict(sorted(terminal_stats_service.get_stats(filename).items(), key=lambda item: item[1], reverse=True))

    total_count = sum(stats.values())

    rows = list()
    for key, value in stats.items():
        rows.append([key, value, value / total_count * 100])

    table = tabulate(rows, headers=['Command', 'Count', '%'], showindex=range(1, len(rows) + 1),
                     floatfmt=(None, None, None, '.2f'))
    print(table)


def _get_env_val_as_bool(val) -> bool:
    return val if type(val) == bool else val.lower() in ['true', 'yes', '1']


def _apply_env_variables_to_config():
    env_debug_val = os.environ.get('DEEPEASY_TERMINAL_STATS_DEBUG')
    if env_debug_val:
        config.DEBUG = _get_env_val_as_bool(env_debug_val)
