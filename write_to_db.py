import sqlite3
import datetime
import Subscriber
import csv
import json
import time


class Database:

    def __init__(self, topic, broker_ip):
        self.topic = topic
        self.broker_ip = broker_ip
        self.sub = Subscriber.Subscribe(self.topic, self.broker_ip)

    def get_data(self):
        data = self.sub.get_single_message()
        self.final_data = data.decode("ASCII")  # in normalen string convertieren
        current_time = datetime.datetime.now()
        self.final_time = current_time.strftime("%d/%m/%Y %H:%M:%S")  # in normales Datum umwandeln

    def write_to_database(self, file):
        self.conn = sqlite3.connect(file, timeout=10)
        self.c = self.conn.cursor()
        self.c.execute("insert into tblLux(lux, datetime) values (?,?)",
                       (self.final_data, self.final_time))
        self.conn.commit()

    def write_to_csv(self):
        file_csv = open("output.csv", "w", newline="")
        writer = csv.writer(file_csv)
        self.c.execute("SELECT * FROM tblLux")
        for row in self.c:
            writer.writerow(row)
        file_csv.close()

    def write_to_json(self):
        self.values = []
        self.c.execute("SELECT * FROM tblLux")
        for row in self.c:
            self.values.append({"id": row[0], "Lux": row[1], "Datum": row[2]})
        j = json.dumps({"Werte": self.values})
        d = json.loads(j)
        file_json = open("output.json", "w")
        json.dump(d, file_json, indent=3)
        file_json.close()


    def main(self, sleep):
        self.get_data()
        self.write_to_database("lux.db")
        print("Daten wurden ind die Datenbank eingetragen: ", self.final_data, self.final_time)
        self.write_to_csv()
        self.write_to_json()
        time.sleep(sleep)



if __name__ == "__main__":
    d1 = Database("SMARTHOME/LUX", "pidevin.local")
    while True:
        d1.main(60) # Sek bis ein neuer Wert in die DB eingetragen wird
