import logging
from flask import request

class RequestFilter(logging.Filter):
    def filter(self, record):
        record.client_ip = request.remote_addr if request else 'unknown'
        return True
