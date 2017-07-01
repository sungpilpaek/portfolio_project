""" Subscribers API

Methods:    [GET]   Returns limited rows of subscribers with an index
            [POST]  Inserts the subscriber's username into the database
"""
from common import message, exception
from flask_restful import Resource, marshal
import json
import fields
import parsers


class Subscribers(Resource):
    def __init__(self, **kwargs):
        self.Subscriber = kwargs['subscriber']

    def get(self):
        args = parsers.GetSubscribers_parser.parse_args()
        index = args['index']

        res, index, status = self.Subscriber().select(index)

        if status == message.TRANSACTION_OK:
            marshaled_res = marshal(res, fields.GetSubscribers_fields)
            data = {'data': marshaled_res, 'index': index}

            return data

        raise exception.InternalServerError()

    def post(self):
        args = parsers.PostSubscribers_parser.parse_args()
        username = args['username']

        status = self.Subscriber().insert(username)

        if status == message.TRANSACTION_OK:
            data = {'status': message.STATUS_OK, 'message': 'Success'}
            
            return data

        elif status == message.TRANSACTION_FAIL_INTEGRITY:
            raise exception.InvalidUsername()

        raise exception.InternalServerError()