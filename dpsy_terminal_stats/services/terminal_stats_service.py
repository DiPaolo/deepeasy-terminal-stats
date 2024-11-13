import enum
from typing import Dict


class Type(enum.Enum):
    UNKNOWN = 0
    ZSH = 1
    BASH = 2

def _get_raw_command(line: str, type: Type):
    match type:
        case Type.ZSH:
            line = line.strip()
            splitted = line.split(';')
            if len(splitted) != 2:
                return None
            
            return splitted[1]
        
        case Type.BASH:
            return line


def get_stats(filename: str) -> Dict[str, int] | None:
    type = Type.UNKNOWN
    if '.zsh_history' in filename:
        type = Type.ZSH
    elif '.bash_history':
        type = Type.BASH

    if type == Type.UNKNOWN:
        print('ERROR failed to find out history type')
        return None

    stats = dict()
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            raw_command = _get_raw_command(line, type)
            if raw_command is None:
                continue

            cmdline = raw_command
            splitted_cmdline = cmdline.split(' ')
            if len(splitted_cmdline) == 0:
                print('ERROR failed to extract command line')
                return None
            
            command = splitted_cmdline[0]
            if command == 'sudo':
                if len(splitted_cmdline) < 2:
                    continue
                command = splitted_cmdline[1]

            if '/' in command:
                command = command.split('/')[-1:][0]

            if command not in stats:
                stats[command] = 0
            stats[command] += 1

    return stats
