# prompy/query.py

from prometheus_api_client import PrometheusConnect
import datetime
import warnings

def prom_init(endpoint, token):
	return PrometheusConnect(url=endpoint, headers={"Authorization": "Bearer {}".format(token)}, disable_ssl=True)

def run(pc, metric, range_min, range_max):
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		return pc.get_metric_range_data(metric_name=metric, start_time=range_min, end_time=range_max)

