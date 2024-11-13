# DeepEasy Terminal Stats

A command line tool that shows up statistics of commands you mostly used in terminal.

## Supported Shells

It's just the very basic support at the moment: MacOS's zsh and Ubuntu's bash. Feel free to ask for any further support: either through issues or contact me [here](#contact). 

## Usage

There is only one way to use the tool for now – by using Python interpreter.

There will be ready-to-use executable later on... probably... 

### Installation Step

```shell
git clone git@github.com:DiPaolo/deepeasy-terminal-stats.git
```

```shell
cd deepeasy-terminal-stats
```

```shell
pip -m virtualenv .venv
```
```shell
source .venv/bin/activate
```

```shell
pip install -r requirements.txt
```

Here it is – it's now ready to use.

### The Actual Usage

To get help/usage:
```shell
python -m dpsy_terminal_stats --help
```

Get statistics for MacOS's zsh shell:
```shell
python -m dpsy_terminal_stats -f ~/.zsh_history
```

Get statistics for Ubuntu's bash shell:
```shell
python -m dpsy_terminal_stats -f ~/.bash_history
```

Output will look like this:
```shell
     Command                                Count      %
---  -----------------------------------  -------  -----
  1  python                                   735  16.58
  2  ffmpeg                                   412   9.29
  3  ffprobe                                  320   7.22
  4  cd                                       318   7.17
  5  ffplay                                   152   3.43
  6  git                                      145   3.27
  7  ll                                       141   3.18
  8  curl                                     126   2.84
  9  docker                                   115   2.59
 10  rm                                        99   2.23
 11  yt-dlp                                    98   2.21
 12  cat                                       89   2.01
 13  mkdir                                     87   1.96
 14  npm                                       83   1.87
 15  alembic                                   70   1.58
 16  conan                                     67   1.51
 17  ssh                                       58   1.31
 18  find                                      56   1.26
 19  scp                                       52   1.17
 20  mv                                        50   1.13
...
```

## Contact

pavel.ditenbir@gmail.com

Telegram: t.me/dipaolo

## License
**MIT License**

Copyright (c) 2024 **Pavel Dittenbier**

Please refer to [License](https://github.com/DiPaolo/deepeasy-terminal-stats/blob/main/LICENSE) page for details.

## Contact
Please feel free to contact me:
- [pavel.ditenbir@gmail.com](mailto:pavel.ditenbir@gmail.com).
- Telegram: https://t.me/dipaolo