import sqlite3
import datetime
import Subscriber
import csv
import time


class Database():

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
        file_csv = open("output.csv", "w")
        writer = csv.writer(file_csv)
        self.c.execute('SELECT * FROM tblLux')
        for row in self.c:
            writer.writerow(row)
        file_csv.close()

    def main(self, sleep):
        try:
            self.get_data()
        except:
            print("Fehler beim empfangen der Daten")
        try:
            self.write_to_database("lux.db")
            print("Daten wurden ind die Datenbank eingetragen: ", self.final_data, self.final_time)
            self.write_to_csv()
            time.sleep(sleep)
        except:
            print("Fehler beim eintragen der Daten in die Datenbank")


if __name__ == "__main__":
    d1 = Database("SMARTHOME/LUX", "pidevin.local")

    while True:
        d1.main(60) # Sek bis ein neuer Wert in die DB eingetragen wird
