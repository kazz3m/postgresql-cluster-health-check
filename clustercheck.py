#!/usr/bin/python3

import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 5555
pgPort = 5000

class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):

    mydb = psycopg2.connect(
        database="postgres",
        port=pgPort,
        host="localhost")

    query = "select pg_is_in_recovery();"
    responseCode = 203
    responseText = "REPLICA"

    try:
      if mydb :
        dbcur = mydb.cursor()
        dbcur.execute(query)
        replica =  dbcur.fetchone()
        print("Server is replica: %s" %(replica))
        if not replica[0] :
            responseCode = 200
            responseText = "MASTER"
            print("I'm a master!")
    except Exception as e :
        print("Error running the query ".format(e))
    finally:
        if dbcur: dbcur.close()
        if mydb: mydb.close()

    self.send_response(responseCode)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(responseText, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
