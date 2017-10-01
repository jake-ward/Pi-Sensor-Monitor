# Development server
# Run this for testing purposes only!

from eventlet import wsgi
import eventlet

from app import app, socketio

app.run(host='0.0.0.0', port=5000)
#wsgi.server(eventlet.listen(('', 5000)), app)
#socketio.run(app, host='0.0.0.0', port=5000)
#app.run()
