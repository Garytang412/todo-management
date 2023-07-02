from json import JSONEncoder
from django.urls import NoReverseMatch
from django.db.models import QuerySet
from datetime import datetime,date, time
from .models import Group
from django.core.serializers.json import DjangoJSONEncoder
from json import JSONDecodeError

class DateEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(o)


class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)


class ModelEncoder(DateEncoder, QuerySetEncoder, JSONEncoder):
    encoders = {}

    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            if hasattr(o, "get_api_url"):
                try:
                    d["href"] = o.get_api_url()
                except NoReverseMatch:
                    pass
            for property in self.properties:
                value = getattr(o, property)
                if property in self.encoders:
                    encoder = self.encoders[property]
                    value = encoder.default(value)
                d[property] = value
            d.update(self.get_extra_data(o))
            return d
        else:
            return super().default(o)

    def get_extra_data(self, o):
        return {}

class DateTimeEncoder(JSONEncoder):
    def default(self,o):
        if isinstance(o,date) or isinstance(o,time):
            return str(o)
        
class GroupListEncoder(ModelEncoder):
    model = Group
    properties = [
        'id',
        'title',
        'create_at',
        'updated_at',
    ]

class GroupDetailEncoder(ModelEncoder):
    model = Group
    properties = [
        'id',
        'title',
        'create_at',
        'updated_at',
    ]