# prompy/__main__.py

from prompy import cli, __app_name__, query, parse

def main():
	cli.app(prog_name=__app_name__)

if __name__ == "__main__":
	main()


