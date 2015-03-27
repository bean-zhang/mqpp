#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    Message Queue Producer
    @author: Bin Zhang
    @email: sjtuzb@gmail.com
'''

import datetime
import json
import pika

from config import *

credentials = pika.PlainCredentials(broker_username, broker_password)
parameters = pika.ConnectionParameters(broker_url, broker_port, vhost, credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

sense_datetime = str(datetime.datetime.now().isoformat())

message = { 'api_key': api_key,
            'gateway_uuid': '12345678-1234-1234-1234-123456789012',
            'gateway_name': 'FYLZ01TEST',
            'sensor_list': [
                {'sensor_uuid': '12345678-5678-5678-5678-123456789012',
                'sensor_name': 'fylz01_temperature',
                'sensor_type': 'temperature',
                'sensor_value': '2',
                'sensor_unit': 'degree centigrade',
                'datetime': sense_datetime,
                'longitude': '121.389701',
                'latitude': '31.085857'},
                {'sensor_uuid': '87654321-5678-5678-5678-123456789012',
                'sensor_name': 'fylz01_humidity',
                'sensor_type': 'humidity',
                'sensor_value': '35',
                'sensor_unit': 'percent',
                'datetime': sense_datetime,
                'longitude': '121.389701',
                'latitude': '31.085857'}]
}

message_json = json.dumps(message)

channel.basic_publish(exchange='exchange', routing_key='routing_key', body=message_json)

print '[t] ' + message_json
connection.close()
