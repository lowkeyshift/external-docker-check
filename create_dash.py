import os

from datadog import initialize, api


API_KEY = os.getenv('API_KEY')
APP_KEY = os.getenv('APP_KEY')

# Variables
IMAGE = os.getenv('IMAGE')

NAME = os.getenv('NAME') #
NAME_1 = os.getenv('NAME_1')
NAME_2 = os.getenv('NAME_2')
NAME_3 = os.getenv('NAME_3')
NAME_4 = os.getenv('NAME_4')
NAME_5 = os.getenv('NAME_5')
NAME_BROKEN_6 = os.getenv('NAME_BROKEN_6')

URL = os.getenv('URL')
URL_PAGE_1 = os.getenv('URL_PAGE_1')
URL_PAGE_2 = os.getenv('URL_PAGE_2')
URL_PAGE_3 = os.getenv('URL_PAGE_3')
URL_PAGE_4 = os.getenv('URL_PAGE_4')
URL_5 = os.getenv('URL_5')
URL_BROKEN_6 = os.getenv('URL_BROKEN_6')

list_dict = {
            NAME:URL,
            NAME_1:URL_PAGE_1,
            NAME_2:URL_PAGE_2,
            NAME_3:URL_PAGE_3,
            NAME_4:URL_PAGE_4,
            NAME_5:URL_5,
            NAME_BROKEN_6:URL_BROKEN_6
            }
options = {
    'api_key': API_KEY,
    'app_key': APP_KEY
}

initialize(**options)

board_title = "{} PKI Dashboard".format(NAME)
description = "A screenboard to measure webpage availability & responsiveness"
width = 1024
for k,v in list_dict.items():
    title = "{}".format(k)
    tags = "url:{}".format(v)
    group = "instance:{},url:{},host:demoexample_CAPITAL_ONE".format(k,v)
    query_graph = "anomalies(avg:http.response_time{%s}, 'basic', 2)" % tags
    log_title = '{} Http Errors'.format(k)
    log_query = 'env:{}'.format(v)
    #group="kayak.com (Main Website), host:demoexample_CAPITAL_ONE"

    widgets = [{
####### COMPANY LOGO IMAGE ########
		'sizing': 'zoom',
		'title_size': 16,
		'title': True,
		'url': IMAGE,
		'margin': '',
		'title_align': 'left',
		'title_text': '',
		'height': 7,
		'width': 41,
		'y': 0,
		'x': 0,
		'type': 'image',
		'isShared': False
	},{
########## END OF LOGO IMAGE ##########
########## FREE TEXT ############
		'title_size': 16,
		'title': True,
		'color': '#774aa4',
		'text': 'Java Application',
		'title_align': 'left',
		'text_align': 'left',
		'title_text': '',
		'height': 6,
		'width': 24,
		'y': 48,
		'x': 143,
		'font_size': 'auto',
		'type': 'free_text',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'color': '#774aa4',
		'text': 'Connection Error Events',
		'title_align': 'left',
		'text_align': 'left',
		'title_text': '',
		'height': 6,
		'width': 24,
		'y': 1,
		'x': 143,
		'font_size': 'auto',
		'type': 'free_text',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'color': '#774aa4',
		'text': 'On-Prem Network/VM',
		'title_align': 'left',
		'text_align': 'left',
		'title_text': '',
		'height': 6,
		'width': 24,
		'y': 1,
		'x': 96,
		'font_size': 'auto',
		'type': 'free_text',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'color': '#774aa4',
		'text': 'DB & Storage ',
		'title_align': 'left',
		'text_align': 'left',
		'title_text': '',
		'height': 6,
		'width': 24,
		'y': 48,
		'x': 96,
		'font_size': 'auto',
		'type': 'free_text',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'color': '#774aa4',
		'text': 'App Latency & App Alerts',
		'title_align': 'left',
		'text_align': 'left',
		'title_text': '',
		'height': 6,
		'width': 29,
		'y': 48,
		'x': 44,
		'font_size': 'auto',
		'type': 'free_text',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'color': '#774aa4',
		'text': 'Website KPI',
		'title_align': 'left',
		'text_align': 'left',
		'title_text': '',
		'height': 6,
		'width': 24,
		'y': 1,
		'x': 44,
		'font_size': 'auto',
		'type': 'free_text',
		'isShared': False
	},{
############ LOGS ############
		'logset': '12',
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': log_title,
		'height': 55,
		'width': 43,
		'query': log_query,
		'x': 0,
		'y': 59,
		'logsetName': '',
		'type': 'log_stream',
		'timeframe': '1d',
		'columns': '["core_host","core_service"]',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'color': '#774aa4',
		'text': 'HTTP ERROR LOGS',
		'title_align': 'left',
		'text_align': 'left',
		'title_text': '',
		'height': 4,
		'width': 24,
		'y': 54,
		'x': 0,
		'font_size': 'auto',
		'type': 'free_text',
		'isShared': False
	},{
		'title_size': 13,
		'tags': ['service:ec2'],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': 'AWS EC2 Availability',
		'height': 8,
		'width': 33,
		'group_by': [],
		'timeframe': '10m',
		'y': 8,
		'x': 109,
		'text_size': 'auto',
		'grouping': 'cluster',
		'type': 'check_status',
		'check': 'aws.status',
		'group': None,
		'isShared': False
	},{
		'title_size': 13,
		'tags': ['*'],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': 'PSQL DB Availability',
		'height': 8,
		'width': 17,
		'group_by': [],
		'timeframe': '10m',
		'y': 55,
		'x': 125,
		'text_size': 'auto',
		'grouping': 'cluster',
		'type': 'check_status',
		'check': 'postgres.can_connect',
		'group': None,
		'isShared': False
	},{
		'title_size': 13,
		'tags': ['*'],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': 'ISCSI Availability',
		'height': 8,
		'width': 15,
		'group_by': [],
		'timeframe': '10m',
		'y': 55,
		'x': 109,
		'text_size': 'auto',
		'grouping': 'cluster',
		'type': 'check_status',
		'check': 'memcache.can_connect',
		'group': None,
		'isShared': False
	},{
		'sizing': 'fit',
		'title_size': 16,
		'title': True,
		'url': 'https://app.datadoghq.com/static/images/saas_logos/bot/amazon_ec2.png',
		'margin': 'small',
		'title_align': 'left',
		'title_text': '',
		'height': 8,
		'width': 12,
		'y': 8,
		'x': 96,
		'type': 'image',
		'isShared': False
	},{
		'sizing': 'fit',
		'title_size': 16,
		'title': True,
		'url': 'https://d30y9cdsu7xlg0.cloudfront.net/png/19487-200.png',
		'margin': 'small',
		'title_align': 'left',
		'title_text': '',
		'height': 8,
		'width': 12,
		'y': 55,
		'x': 96,
		'type': 'image',
		'isShared': False
	},{
######## BEGINNING OF CHECKS ##########
		'title_size': 13,
		'tags': [tags],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 12,
		'group_by': [],
		'timeframe': '10m',
		'y': 14,
		'x': 0,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
        'title_size': 13,
        'tags': [tags],
        'title': True,
        'title_text': title,
        'height': 7,
        'width': 16,
        'group_by': [],
        'timeframe': '10m',
        'y': 14,
        'x': 27,
        'text_size': 'auto',
        'grouping': 'check',
        'type': 'check_status',
        'check': 'http.can_connect',
        'group': group,
        'isShared': False,
    },{
		'title_size': 13,
		'tags': [tags],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 12,
		'group_by': [],
		'timeframe': '10m',
		'y': 22,
		'x': 0,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': [],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 12,
		'group_by': [],
		'timeframe': '10m',
		'y': 30,
		'x': 0,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': [],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 13,
		'group_by': [],
		'timeframe': '10m',
		'y': 14,
		'x': 13,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': [],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 13,
		'group_by': [],
		'timeframe': '10m',
		'y': 22,
		'x': 13,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': [],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 13,
		'group_by': [],
		'timeframe': '10m',
		'y': 30,
		'x': 13,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': [],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 13,
		'group_by': [],
		'timeframe': '10m',
		'y': 38,
		'x': 13,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': [],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 12,
		'group_by': [],
		'timeframe': '10m',
		'y': 38,
		'x': 0,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': ['*'],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 16,
		'group_by': [],
		'timeframe': '10m',
		'y': 46,
		'x': 27,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': ['*'],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 16,
		'group_by': [],
		'timeframe': '10m',
		'y': 38,
		'x': 27,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': ['*'],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 16,
		'group_by': [],
		'timeframe': '10m',
		'y': 30,
		'x': 27,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
		'title_size': 13,
		'tags': ['*'],
		'title': True,
		'title_align': 'center',
		'text_align': 'center',
		'title_text': title,
		'height': 7,
		'width': 16,
		'group_by': [],
		'timeframe': '10m',
		'y': 22,
		'x': 27,
		'text_size': 'auto',
		'grouping': 'check',
		'type': 'check_status',
		'check': 'http.can_connect',
		'group': group,
		'isShared': False
	},{
######## BEGINNING OF CHECKS ##########
######### BEGINNING OF NOTES #########
		'title_size': 16,
		'title': True,
		'refresh_every': 30000,
		'tick_pos': '50%',
		'title_align': 'left',
		'tick_edge': 'left',
		'text_align': 'center',
		'title_text': '',
		'height': 5,
		'bgcolor': 'blue',
		'html': 'Main Site',
		'y': 8,
		'x': 27,
		'font_size': '24',
		'tick': False,
		'type': 'note',
		'width': 16,
		'auto_refresh': False,
		'isShared': False
	},{

		'title_size': 16,
		'title': True,
		'refresh_every': 30000,
		'tick_pos': '50%',
		'title_align': 'left',
		'tick_edge': 'left',
		'text_align': 'center',
		'title_text': '',
		'height': 5,
		'bgcolor': 'blue',
		'html': 'CDNs',
		'y': 8,
		'x': 0,
		'font_size': '24',
		'tick': False,
		'type': 'note',
		'width': 12,
		'auto_refresh': False,
		'isShared': False
	},{

		'title_size': 16,
		'title': True,
		'refresh_every': 30000,
		'tick_pos': '50%',
		'title_align': 'left',
		'tick_edge': 'left',
		'text_align': 'center',
		'title_text': '',
		'height': 5,
		'bgcolor': 'blue',
		'html': 'BI Tools',
		'y': 8,
		'x': 13,
		'font_size': '24',
		'tick': False,
		'type': 'note',
		'width': 13,
		'auto_refresh': False,
		'isShared': False
	},{

		'title_size': 16,
		'title': True,
		'refresh_every': 30000,
		'tick_pos': '50%',
		'title_align': 'left',
		'tick_edge': 'left',
		'text_align': 'center',
		'title_text': '',
		'height': 7,
		'bgcolor': 'blue',
		'html': 'SSL',
		'y': 46,
		'x': 0,
		'font_size': '24',
		'tick': False,
		'type': 'note',
		'width': 12,
		'auto_refresh': False,
		'isShared': False
	},{
######### END OF NOTES ###########
######### BEGINNING OF EVENTS ###########
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Http Errors',
		'height': 27,
		'width': 53,
		'global_timeframe_controls': False,
		'query': 'http_check ',
		'tags_execution': 'and',
		'timeframe': '1h',
		'y': 19,
		'x': 143,
		'type': 'event_stream',
		'event_size': 'l',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Http Error Events',
		'height': 9,
		'width': 53,
		'global_timeframe_controls': False,
		'query': 'http_check',
		'tags_execution': 'and',
		'timeframe': '1h',
		'y': 8,
		'x': 143,
		'type': 'event_timeline',
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'App Alerts',
		'height': 35,
		'width': 51,
		'global_timeframe_controls': False,
		'query': 'tags:monitor status:error boyan "application latency" ',
		'tags_execution': 'and',
		'timeframe': '4h',
		'y': 77,
		'x': 44,
		'type': 'event_stream',
		'event_size': 'l',
		'isShared': False
	},{
######### END OF EVENTS ###########
######### BEGINNING OF Query Value ###########
		'autoscale': True,
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'SSL Days Left',
		'height': 5,
		'tile_def': {
			'viz': 'query_value',
			'requests': [{
				'q': 'avg:http.ssl.days_left{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': None,
				'conditional_formats': [{
					'palette': 'red_on_white',
					'value': '200',
					'comparator': '<='
				}, {
					'palette': 'white_on_yellow',
					'value': None,
					'comparator': '>='
				}, {
					'palette': 'white_on_green',
					'value': None,
					'comparator': '<'
				}]
			}],
			'autoscale': True,
			'custom_unit': 'days',
			'precision': '0'
		},
		'width': 13,
		'timeframe': '1h',
		'y': 46,
		'x': 13,
		'legend_size': '0',
		'type': 'query_value',
		'legend': False,
		'isShared': False
	},{
		'x': 96,
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'DB Connections',
		'height': 6,
		'tile_def': {
			'viz': 'query_value',
			'requests': [{
				'q': 'avg:postgresql.connections{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': None,
				'conditional_formats': [{
					'palette': 'white_on_red',
					'comparator': '>=',
					'value': '20'
				}, {
					'palette': 'white_on_yellow',
					'comparator': '>=',
					'value': None
				}, {
					'palette': 'white_on_green',
					'comparator': '<=',
					'value': '15'
				}]
			}],
			'autoscale': True,
			'precision': '0'
		},
		'width': 14,
		'timeframe': '1h',
		'y': 64,
		'autoscale': True,
		'legend_size': '0',
		'type': 'query_value',
		'legend': False,
		'isShared': False
	},{
		'x': 112,
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Storage Space',
		'height': 6,
		'tile_def': {
			'viz': 'query_value',
			'requests': [{
				'q': 'avg:system.disk.free{role:db}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': None,
				'conditional_formats': [{
					'palette': 'white_on_red',
					'comparator': '<=',
					'value': '10'
				}, {
					'palette': 'white_on_yellow',
					'comparator': '>=',
					'value': None
				}, {
					'palette': 'white_on_green',
					'comparator': '>=',
					'value': '40'
				}]
			}],
			'autoscale': True,
			'precision': '0'
		},
		'width': 14,
		'timeframe': '1h',
		'y': 64,
		'autoscale': True,
		'legend_size': '0',
		'type': 'query_value',
		'legend': False,
		'isShared': False
	},{
		'x': 128,
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Storage Used',
		'height': 6,
		'tile_def': {
			'viz': 'query_value',
			'requests': [{
				'q': 'avg:system.disk.used{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': None,
				'conditional_formats': [{
					'palette': 'white_on_red',
					'comparator': '>=',
					'value': '200000000000'
				}, {
					'palette': 'white_on_yellow',
					'comparator': '>=',
					'value': None
				}, {
					'palette': 'white_on_green',
					'comparator': '<=',
					'value': '60000000000'
				}]
			}],
			'autoscale': True,
			'precision': '0'
		},
		'width': 14,
		'timeframe': '1h',
		'y': 64,
		'autoscale': True,
		'legend_size': '0',
		'type': 'query_value',
		'legend': False,
		'isShared': False
	},{
		'x': 44,
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Page Latency',
		'height': 6,
		'tile_def': {
			'viz': 'query_value',
			'requests': [{
				'q': 'avg:http.response_time{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': None,
				'conditional_formats': [{
					'palette': 'white_on_red',
					'comparator': '>=',
					'value': '1'
				}, {
					'palette': 'white_on_yellow',
					'comparator': '>=',
					'value': '0.80'
				}, {
					'palette': 'white_on_green',
					'comparator': '<=',
					'value': '1'
				}]
			}],
			'autoscale': True,
			'custom_unit': 'secs'
		},
		'width': 16,
		'timeframe': '1h',
		'y': 8,
		'autoscale': True,
		'legend_size': '0',
		'type': 'query_value',
		'legend': False,
		'isShared': False
	},{
		'x': 62,
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Infra Latency',
		'height': 6,
		'tile_def': {
			'viz': 'query_value',
			'requests': [{
				'q': 'avg:gunicorn.request.duration.avg{*}+avg:cassandra.db.recent_read_latency_micros{*}+avg:cassandra.db.recent_write_latency_micros{*}+avg:redis.info.latency_ms{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': [{
					'palette': 'white_on_green',
					'value': '100',
					'comparator': '<='
				}, {
					'palette': 'white_on_yellow',
					'value': '100',
					'comparator': '>'
				}, {
					'palette': 'white_on_red',
					'value': '250',
					'comparator': '>'
				}]
			}],
			'autoscale': False,
			'custom_unit': 'ms',
			'markers': [{
				'dim': 'y',
				'min': 2000,
				'max': None,
				'value': 'y > 2000',
				'label': 'Danger Zone',
				'type': 'error dashed'
			}]
		},
		'width': 15,
		'timeframe': '1h',
		'y': 8,
		'autoscale': True,
		'legend_size': '0',
		'type': 'query_value',
		'legend': False,
		'isShared': False
	},{

		'x': 79,
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Web Latency',
		'height': 6,
		'tile_def': {
			'viz': 'query_value',
			'requests': [{
				'q': 'avg:haproxy.backend.response.time{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': [{
					'palette': 'white_on_green',
					'comparator': '<=',
					'value': 1000
				}, {
					'palette': 'white_on_yellow',
					'comparator': '>',
					'value': 1000
				}, {
					'palette': 'white_on_red',
					'value': 2500,
					'comparator': '>'
				}]
			}],
			'autoscale': False,
			'custom_unit': None,
			'markers': [{
				'dim': 'y',
				'min': 2000,
				'max': None,
				'value': 'y > 2000',
				'label': 'Danger Zone',
				'type': 'error dashed'
			}]
		},
		'width': 16,
		'timeframe': '1h',
		'y': 8,
		'autoscale': True,
		'legend_size': '0',
		'type': 'query_value',
		'legend': False,
		'isShared': False
	},{
######### END OF Query Value ###########
######### BEGINNING OF Graphs ###########
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Avg Page Load w/ Anomaly',
		'height': 13,
		'tile_def': {
			'viz': 'timeseries',
			'requests': [{
				'q': query_graph,
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': []
			}],
			'autoscale': True
		},
		'width': 51,
		'timeframe': '1h',
		'y': 17,
		'x': 44,
		'legend_size': '0',
		'type': 'timeseries',
		'legend': False,
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'DB Connetions',
		'height': 19,
		'tile_def': {
			'viz': 'timeseries',
			'requests': [{
				'q': 'avg:postgresql.connections{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': []
			}],
			'autoscale': True
		},
		'width': 46,
		'timeframe': '1h',
		'y': 93,
		'x': 96,
		'legend_size': '0',
		'type': 'timeseries',
		'legend': False,
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'AWS EBS R/W Ops',
		'height': 13,
		'tile_def': {
			'viz': 'timeseries',
			'requests': [{
				'q': 'avg:aws.ec2.ebswrite_ops{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': []
			}, {
				'q': 'avg:aws.ec2.ebsread_ops{*}',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line'
			}],
			'autoscale': True
		},
		'width': 46,
		'timeframe': '1y',
		'y': 33,
		'x': 96,
		'legend_size': '0',
		'type': 'timeseries',
		'legend': False,
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'DB Connetions',
		'height': 17,
		'tile_def': {
			'viz': 'timeseries',
			'requests': [{
				'q': 'avg:postgresql.connections{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': []
			}],
			'autoscale': True
		},
		'width': 46,
		'timeframe': '1h',
		'y': 73,
		'x': 96,
		'legend_size': '0',
		'type': 'timeseries',
		'legend': False,
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Overall App Latency',
		'height': 19,
		'tile_def': {
			'autoscale': False,
			'yaxis': {
				'scale': 'sqrt'
			},
			'custom_unit': 'ms',
			'markers': [{
				'dim': 'y',
				'min': 0,
				'max': 250,
				'value': '0 < y < 250',
				'label': 'Healthy',
				'type': 'ok dashed'
			}, {
				'dim': 'y',
				'min': 250,
				'max': 500,
				'value': '250 < y < 500',
				'label': 'Warning',
				'type': 'warning dashed'
			}, {
				'dim': 'y',
				'min': 500,
				'max': None,
				'value': 'y > 500',
				'label': 'Poor',
				'type': 'error dashed'
			}],
			'viz': 'timeseries',
			'requests': [{
				'q': 'avg:trace.dogweb.base.before.duration{*}+avg:cassandra.db.recent_read_latency_micros{*}+avg:cassandra.db.recent_write_latency_micros{*}+avg:redis.info.latency_ms{*}+avg:gunicorn.request.duration.avg{*}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': [{
					'palette': 'white_on_green',
					'comparator': '<=',
					'value': 1000
				}, {
					'palette': 'white_on_yellow',
					'comparator': '>',
					'value': 1000
				}, {
					'palette': 'white_on_red',
					'comparator': '>',
					'value': 1500
				}]
			}],
			'events': [{
				'q': 'tags:monitor status:error boyan "application latency" ',
				'tags_execution': 'and'
			}]
		},
		'width': 51,
		'timeframe': '4h',
		'y': 55,
		'x': 44,
		'legend_size': '0',
		'type': 'timeseries',
		'legend': False,
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'Internal SNMP I/O Errors',
		'height': 13,
		'tile_def': {
			'viz': 'timeseries',
			'requests': [{
				'q': "anomalies(avg:snmp.ifInErrors{*}, 'basic', 2)",
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': []
			}, {
				'q': "anomalies(avg:snmp.ifOutErrors{*}, 'basic', 2)",
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line'
			}],
			'autoscale': True
		},
		'width': 46,
		'timeframe': '1h',
		'y': 17,
		'x': 96,
		'legend_size': '0',
		'type': 'timeseries',
		'legend': False,
		'isShared': False
	},{
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'title_text': 'AVG Page load by URL',
		'height': 13,
		'tile_def': {
			'viz': 'timeseries',
			'requests': [{
				'q': 'avg:http.response_time{*} by {url}',
				'aggregator': 'avg',
				'style': {
					'width': 'normal',
					'palette': 'dog_classic',
					'type': 'solid'
				},
				'type': 'line',
				'conditional_formats': []
			}],
			'autoscale': True
		},
		'width': 51,
		'timeframe': '1h',
		'y': 33,
		'x': 44,
		'legend_size': '0',
		'type': 'timeseries',
		'legend': False,
		'isShared': False
######### END OF Graphs ###########
	},{
######### APM #########
		'mustShowErrors': True,
		'height': 59,
		'mustShowBreakdown': True,
		'text_size': 'auto',

		'sizeVersion': 'medium',
		'title_size': 16,
		'title': True,
		'title_align': 'left',
		'text_align': 'left',
		'width': 53,
		'serviceName': 'servlet.request',
		'env': 'staging',
		'timeframe': '1h',
		'type': 'trace_service',
		'isShared': False,
		'mustShowResourceList': False,
		'serviceService': 'coffee-house',
		'title_text': 'coffee-house #env:staging',
		'mustShowHits': True,
		'mustShowDistribution': True,
		'mustShowLatency': True,
		'layoutVersion': 'two_column',
		'y': 55,
		'x': 143
	},]

api.Screenboard.create(board_title=board_title,
                       description=description,
                       widgets=widgets,
                       width=width)
