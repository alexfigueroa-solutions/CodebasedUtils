import os
import click
import logging
from colorama import init, Fore
init(autoreset=True)

# Setup logging
logging.basicConfig(filename='logs/codespace_utils.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@click.group()
def util():
    """Utility commands."""
    pass

@util.command(name="printdir")  # Rename the command to 'printdir'
@click.argument('path', default='.')
@click.option('--exclude', default='', help='File patterns to exclude (e.g. *.log)')

def dirprint(path, exclude):
    """Prints a directory structure, ignoring nonessential files."""
    def should_exclude(file_name):
        return file_name.startswith('.') or (exclude and file_name.endswith(exclude))

    def print_directory_structure(startpath):
        for root, dirs, files in os.walk(startpath):
            dirs[:] = [d for d in dirs if not should_exclude(d)]
            files = [f for f in files if not should_exclude(f)]

            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print(f'{Fore.BLUE}{indent}{os.path.basename(root)}/')

            subindent = ' ' * 4 * (level + 1)
            for file in files:
                print(f'{Fore.GREEN}{subindent}{file}')

    try:
        print_directory_structure(path)
    except FileNotFoundError:
        logging.error("The specified directory doesn't exist.")
        click.echo(f"{Fore.RED}Error: The specified directory doesn't exist.")
    except PermissionError:
        logging.error("Permission denied for reading the directory.")
        click.echo(f"{Fore.RED}Error: Permission denied for reading the directory.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        click.echo(f"{Fore.RED}An unexpected error occurred. Check logs for details.")

if __name__ == "__main__":
    util()
