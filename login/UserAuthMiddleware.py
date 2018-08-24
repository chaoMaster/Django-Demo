# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class UserLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/login/' or request.path == '/regist/':
            return None
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
