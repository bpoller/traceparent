# -*- coding: utf-8 -*-
from django.http import QueryDict

from rest_framework import serializers
from rest_framework.reverse import reverse


class HyperlinkedFilterField(serializers.Field):

    def __init__(self, *args, **kwargs):

        self.view_name     = kwargs.pop('view_name')
        self.format        = kwargs.pop('format', None)
        self.lookup_params = kwargs.pop('lookup_params')
        self.lookup_test   = kwargs.pop('lookup_test', None)

        return super(HyperlinkedFilterField, self).__init__(*args, **kwargs)

    def field_to_native(self, o, *args, **kwargs):

        if self.lookup_test and not self.lookup_test(o): return None

        view_name = self.view_name
        request   = self.context.get('request', None)
        format    = self.format or self.context.get('format', None)

        query = QueryDict('', mutable=True)
        for key, field in self.lookup_params.items():
            query[key] = getattr(o, field)

        return '%s?%s' % (reverse(view_name, request=request, format=format),
                    query.urlencode())


