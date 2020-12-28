#!/usr/bin/python3

from oligo import Iber
from datetime import date, timedelta
import paho.mqtt.publish as mqttpublish
import json

consumo = []

connection = Iber()
connection.login("user-iberdrola", "password-iberdrola")

from_date = date.today() - timedelta(days=1)
until_date = date.today() - timedelta(days=1)

consumo = connection.consumption(from_date, until_date)

consumo24h = sum(consumo)
print(consumo24h)

mqttdata = json.dumps({
	"date": from_date,
	"Iberdrola24h": int(consumo24h)
	})

mqttpublish.single("sensors/oligo/Iberdrola24h", mqttdata, hostname="hostname-broker-mqtt")
