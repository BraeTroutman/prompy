# prompy/cli.py

from typing import Optional
import typer
from prompy import __app_name__, __version__, query, parse
from datetime import datetime
from prometheus_api_client import MetricRangeDataFrame
import pyarrow as pa
import pyarrow.parquet as pq

DT_FORMAT="%Y-%m-%d %H:%M:%S.%f"

app = typer.Typer()

@app.command()
def run(
	metric: str = typer.Option("up", "--metric", "-m"),
	min: str = typer.Option("2022-05-01 00:00:00.00", "--min-time", "-a"),
	max: str = typer.Option("2022-05-31 00:00:00.00", "--max-time", "-b"),
	infig: str = typer.Option("input-config.yaml", "--input-config", "-i"),
	outfig: str = typer.Option("output-config.yaml", "--output-config", "-o"),
	) -> None :
	
	typer.echo("parsing timestamps")

	start = datetime.strptime(min, DT_FORMAT)
	end = datetime.strptime(max, DT_FORMAT)

	typer.echo("parsing config files")

	input_config = parse.inconfig(infig)
	output_config = parse.outconfig(outfig)
	
	typer.echo("running prom query")

	pc = query.prom_init(input_config['endpoint'].data, input_config['token'].data)
	res = query.run(pc, metric, start, end)
	
	typer.echo(f"writing query results to file {output_config['name'].data}")
	MetricRangeDataFrame(res).to_parquet(output_config['name'].data, use_deprecated_int96_timestamps=True)
	
	raise typer.Exit()

def _version_callback(value: bool) -> None:
	if value:
		typer.echo(f"{__app_name__} v{__version__}")
		raise typer.Exit()

@app.callback()
def main (
	version: Optional[bool] = typer.Option(
		None, 
		"--version",
		"-v",
		help="Show application name and version",
		callback=_version_callback,
		is_eager=True,
	)
) -> None:
	return

