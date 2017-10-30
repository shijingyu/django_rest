# -*- coding: utf-8 -*-
# @Time    : 17-10-28 上午9:40
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : serializers.py
# @Describe:
# @Software: PyCharm

from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
