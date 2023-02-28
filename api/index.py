from http.server import BaseHTTPRequestHandler
from ytmurl.get import get as get_ytmrul
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    parsed_url = urlparse(self.path)

    # retrieve query
    query = parse_qs(parsed_url.query)
    try:
      response = get_ytmrul(query['q'][0], (int(query['dmin'][0]), int(query['dmax'][0])))
    except:
      self.send_response(500)
      return

    # Send the HTML message
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(response.encode())
    return
