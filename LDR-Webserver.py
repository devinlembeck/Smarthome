from bottle import Bottle, template
import sqlite3
import write_to_db

class LDR_Webserver:

    def __init__(self):
        self.server = Bottle()
        self.d1 = write_to_db.Database("SMARTHOME/LUX", "pidevin.local")
        self.host = "localhost"
        self.port = 8080
        self.routes()

    def start_server(self):
        self.server.run(host=self.host, port=self.port)

    def routes(self):
        self.server.route("/",callback=self.luxpage)

    def luxpage(self):
        db = sqlite3.connect('lux.db')
        c = db.cursor()
        c.execute("SELECT lux, datetime FROM tblLux")
        data = c.fetchall()
        c.close()
        output = template('lux_page_smarthome', rows=data)
        return output

if __name__ == "__main__":
    s1 = LDR_Webserver()
    s1.start_server()