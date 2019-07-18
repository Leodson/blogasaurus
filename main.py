# dev_appserver.py app.yaml

import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        index_template=jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        index_template=jinja_env.get_template('templates/y_favorite_candy.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

app = webapp2.WSGIApplication([
    ('/', IndexHandler)
], debug=True)
