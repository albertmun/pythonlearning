import sys
import io
from app import socketio
from flask import request

# Store a namespace (dict) for each client
user_namespaces = {}

@socketio.on('connect')
def handle_connect():
    user_namespaces[request.sid] = {}

@socketio.on('disconnect')
def handle_disconnect():
    user_namespaces.pop(request.sid, None)

@socketio.on('execute')
def handle_execute(data):
    code = data['code']
    namespace = user_namespaces.get(request.sid, {})
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = sys.stderr = mystdout = io.StringIO()
    try:
        # Try eval first for expressions
        try:
            result = eval(code, namespace)
            if result is not None:
                print(repr(result))
        except SyntaxError:
            exec(code, namespace)
        except Exception as e:
            print(e)
        output = mystdout.getvalue()
        socketio.emit('output', {'output': output}, to=request.sid)
    except Exception as e:
        socketio.emit('output', {'output': str(e)}, to=request.sid)
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        user_namespaces[request.sid] = namespace 