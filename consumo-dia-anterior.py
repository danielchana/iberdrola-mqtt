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

print(consumo)

consumo24h = numpysum(consumo)
print(consumo24h)

mqttdata = json.dumps({
	"date": from_date,
	"consumo24h": int(consumo24h)
	})

mqttpublish.single("sensors/oligo/consumo24h", mqttdata, hostname="hostname")
