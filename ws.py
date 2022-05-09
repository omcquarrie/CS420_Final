import cherrypy
import score
import game
import json

#docker build -t python-ws .
#docker run -p 8080:8080 python-ws

#declares "Movie" object
m = score.Score()
game_instance = game.SnakeAndApple()

class MyWebService(object):
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def score(self, score):

        #accepts output from Movie object and formats to json
        #(though it doesn't work perfectly when formatting)
        output = m.run(score)
        jsonContent = json.dumps(output)
        return jsonContent

    def game(self):
        output = game_instance.mainloop()

    
if __name__ == '__main__':

    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())
