from lab3.wtiproj03_ETL import pivot_movie_all_genres
from flask import jsonify, make_response
import cherrypy
import json
import random

data_frame, all_genres = pivot_movie_all_genres()
data_frame = data_frame.fillna(0)


@cherrypy.expose()
@cherrypy.tools.json.out()
class rating(object):
    @cherrypy.tools.accept(media='text/plain')
    def POST(self, **data):
        global df
        print(data)
        df = df.append(data, ignore_index=True)
        return df.to_dict(orient='records')


@cherrypy.expose
@cherrypy.tools.json_out()
class ratings(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        if data_frame.empty:
            return jsonify('empty')
        else:
            json_files = json.loads(data_frame.to_json(orient='records'))
            return make_response(jsonify(json_files), 200)

    def DELETE(self):
        global data_frame
        data_frame = data_frame.iloc[0:0]
        if data_frame.empty:
            return make_response("removed", 200)


@cherrypy.expose
@cherrypy.tools.json_out()
class get_user(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        user = {}
        for x in all_genres:
            user[x] = random.uniform(0, 5)
        return user


@cherrypy.expose
@cherrypy.tools.json_out()
class all_users(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self, user):
        users = {}
        for x in all_genres:
            users[x] = random.uniform(0, 5)
        users['userID'] = user
        return users


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.tree.mount(rating(), '/rating', conf)
    cherrypy.tree.mount(ratings(), '/ratings', conf)
    cherrypy.tree.mount(get_user(), '/ratings/all-users', conf)
    cherrypy.tree.mount(all_users(), '/ratings/', conf)
    cherrypy.engine.start()
