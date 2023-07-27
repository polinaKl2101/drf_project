import re
from rest_framework import serializers


def validated_link(value):

    link_regex = r'^https?:\/\/(?:www\.)?youtube\.com\/watch\?v=[\w-]{11}$'
    if not re.match(link_regex, value):
        raise serializers.ValidationError('Недопустимая ссылка')
    return value

