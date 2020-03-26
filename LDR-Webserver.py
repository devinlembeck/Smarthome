import bottle
import sqlite3
import write_to_db
import os
class LDR_Webserver:

    def __init__(self, topic, broker_ip):
        self.server = bottle.Bottle()
        self.d1 = write_to_db.Database(topic, broker_ip)
        self.host = "localhost"
        self.port = 8080
        self.routes()

    def start_server(self):
        self.server.run(host=self.host, port=self.port)

    def routes(self):
        self.server.route("/", callback=self.luxpage)  # mainpage
        self.server.route("/get_csv", callback=self.get_csv)  # csv download
        self.server.route("/get_json", callback=self.get_json)  # json download

    def luxpage(self):
        db = sqlite3.connect('lux.db')
        c = db.cursor()
        c.execute("SELECT lux, datetime FROM tblLux")
        data = c.fetchall()
        c.close()
        output = bottle.template('lux_page_smarthome', rows=data)
        return output

    def get_csv(self):
        return bottle.static_file("output.csv", root=os.getcwd(), download="output.csv")

    def get_json(self):
        return bottle.static_file("output.json", root=os.getcwd(), download="output.json")


if __name__ == "__main__":
    s1 = LDR_Webserver("SMARTHOME/LUX", "pidevin.local")
    s1.start_server()
