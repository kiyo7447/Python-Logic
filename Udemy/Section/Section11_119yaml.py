# -*- coding: utf-8 -*-

import yaml

with open('config.yaml', 'w') as yaml_file:
    yaml.dump({'DEFAULT': {'debug': False}, 
               'web_server': {'host': '127.0.0.1', 'port': 80},
                'db_server': {'host': '127.0.0.1', 'port': 3306}}, 
                yaml_file, default_flow_style=False)

with open('config.yaml', 'r') as yaml_file:
    config = yaml.load(yaml_file)
    print(config['DEFAULT']['debug'])
    print(config['web_server']['host'])
    print(config['web_server']['port'])
    print(config['db_server']['host'])
    print(config['db_server']['port'])

