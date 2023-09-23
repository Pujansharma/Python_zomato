from flask_socketio import SocketIO, emit, join_room, disconnect
from flask import current_app
from app import routes  # Import your Flask app instance
from app.socketio import init_socketio
socketio = SocketIO()

def init_socketio(app):
    socketio.init_app(app)

    @socketio.on('connect')
    def handle_connect():
        # Handle client connection (e.g., authenticate user if needed)
        print('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        # Handle client disconnection (e.g., cleanup or logging)
        print('Client disconnected')

    @socketio.on('join_room')
    def join_room(data):
        room = data['room']  # Room name (e.g., order ID) sent by the client
        join_room(room)
        print(f'Client joined room: {room}')

    @socketio.on('order_status_update')
    def handle_order_status_update(data):
        room = data['room']  # Room name (e.g., order ID) sent by the client
        status = data['status']  # New order status
        # Update the order status in the database
        # Emit a message to the specific room with the updated status
        emit('update_order_status', {'status': status}, room=room)
init_socketio(routes)

if __name__ == '__main__':
    socketio.run(routes)