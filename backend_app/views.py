from rest_framework import viewsets
from .models import Status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views
from subprocess import Popen, PIPE
import os
import json

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.filter()
    serializer_class = StatusSerializer

class ChangeStatus(APIView):
	def get(self, request, format=None):
		sudo_password = 'Hackme1337'
		status = None
		for obj in Status.objects.filter(id=1):
			status = obj.on_off
		if status == False:
			command = 'sudo snort -D -q -c /etc/snort/snort.conf -i wlan1'.split()
			p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
			sudo_prompt = p.communicate(sudo_password + '\n')[1]
			Status.objects.filter(id=1).update(on_off=True)
		else:
			command = 'sudo pkill snort'.split()
			p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
			sudo_prompt = p.communicate(sudo_password + '\n')[1]
			Status.objects.filter(id=1).update(on_off=False)
		return Response({"Status": 'Ok'})

class GetAlerts(APIView):
	def get(self, request, format=None):
		alerts_file = open("/var/log/snort/alert")
		alerts = alerts_file.read()
		alerts_file.close()
		return Response({"all_allerts": alerts})


class IptablesAdd(APIView):
	def post(self, request, format=None):

		if request.method == 'POST':
			sudo_password = 'Hackme1337'
			command_full = 'sudo iptables ' + str(request.data['rule'])
			command = command_full.split()
			p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
			sudo_prompt = p.communicate(sudo_password + '\n')[1]
			return Response({"Status": 'Ok'})