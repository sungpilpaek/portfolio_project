"""Collection of APIs
"""
from common import message, exception
from flask_restful import Resource, marshal
import json
import fields
import parsers


class GetSubscribers(Resource):
    def __init__(self, **kwargs):
        self.query_all = kwargs['query_all']

    def get(self):
        args = parsers.GetSubscribers_parser.parse_args()
        index = args['index']
        res, index, status = self.query_all(index)
        if status == message.TRANSACTION_OK:
            marshaled_res = marshal(res, fields.GetSubscribers_fields)
            data = {'data': marshaled_res, 'index': index}
            return json.dumps(data)

        raise exception.InternalServerError()


class PostSubscribers(Resource):
    def __init__(self, **kwargs):
        self.Subscriber = kwargs['subscriber']

    def post(self):
        args = parsers.PostSubscribers_parser.parse_args()
        username = args['username']
        status = self.Subscriber(username).insert_to_db()
        if status == message.TRANSACTION_OK:
            return username

        elif status == message.TRANSACTION_FAIL_INTEGRITY:
            raise exception.InvalidUsername()