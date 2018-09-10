
# Subject

Écrire un script myls.py (variante simple de ls). Ce script s'exécute à la ligne de commande en lui passant le chemin d'un dossier, il liste alors les fichiers présents dans ce dossier avec leur taille. La taille peut être indiquée en bytes (B), kB, MB, GB, selon une option facultative --unit passée en paramètre.

## Sample

./myls.py /some/path/to/folder/ --unit kB
foo.txt           4.2 kB
bar.zip        1042.5 kB

# Project Dependencies

* [Python](https://www.python.org/downloads/) 3.5 >=
* [Pytest](https://docs.pytest.org/en/latest/) 3.0.7 >=
* [Humanize](https://pypi.org/project/humanize/) 0.5.1 >=

## Installation

##### Clone the project
`$ git clone https://github.com/christophe-martel/xxx`

##### Setting up the environment

`cd [your_folder_name]/myls`

`python -m pip install -r ./bin/requirements.txt`

## Usage

### Launch

`cd [your_folder_name]/myls`

`python bin/__init__.py --help` (Will print the help for program)
`python bin/__init__.py . --unit MB`

### Launch tests

`cd [your_folder_name]`
`python  -m pytest testing/tests.py`
