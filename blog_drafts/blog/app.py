from flask import Flask, jsonify

app = Flask(__name__)

# Add this root route - this handles http://127.0.0.1:5000/
@app.route('/')
def home():
    return '''
    <html>
    <head><title>AFK Server Finder</title></head>
    <body>
        <h1>🎮 Steal a Brainrot - AFK Server Finder</h1>
        <p>Flask is working! 🎉</p>
        <p>Test the API: <a href="/api/afk-servers">/api/afk-servers</a></p>
        <p>Or <a href="/api/find-servers">click here</a> to find AFK servers</p>
    </body>
    </html>
    '''

# Your AFK server endpoint
@app.route('/api/afk-servers')
def get_afk_servers():
    servers = [
        {"name": "Steal-A-Brainrot-1", "afk_players": 2, "total_players": 8},
        {"name": "Steal-A-Brainrot-3", "afk_players": 1, "total_players": 12},
        {"name": "Steal-A-Brainrot-7", "afk_players": 3, "total_players": 6}
    ]
    return jsonify({
        'success': True,
        'servers_found': len(servers),
        'servers': servers
    })

# Add this new route that matches what we discussed earlier
@app.route('/api/find-servers', methods=['GET'])
def find_servers():
    servers = [
        {"name": "Brainrot-Server-ABC123", "afk_count": 2, "join_link": "roblox://placeId=123456789"},
        {"name": "Brainrot-Server-DEF456", "afk_count": 1, "join_link": "roblox://placeId=123456789"},
        {"name": "Brainrot-Server-GHI789", "afk_count": 3, "join_link": "roblox://placeId=123456789"}
    ]
    return jsonify({
        'success': True,
        'message': 'Found servers with AFK players!',
        'servers': servers
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)