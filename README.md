# Multi-threading-using-Python-for-Chat-Application
Developed a simple console‐based chat application in Python where multiple users can communicate with each other using threads.

Server:
-> Listens for connections and starts a new thread for each connected client.
-> The 'handle_client' function manages message receipt and broadcasts messages or notifications when a user exits.

Client:
-> Connects to the server and listens for incoming messages in a separate thread while allowing the user to send messages.

Python using socket and threading:
Step 1: Setting Up the Server
-> Create a Server Socket: This will listen for incoming connections.
-> Handle Multiple Clients: Use threading to handle each client connection.

Step 2: Broadcast Messages
-> Store Connected Clients: Maintain a list of connected clients to broadcast messages.
-> Send Messages: Implement a function to send messages to all connected clients.

Step 3: Handle Exit Command
-> Detect Exit Command: Listen for the "exit" command from any client.
-> Remove Client: When a client sends "exit", remove them from the list of connected clients.
-> Notify Other Clients: Inform all other clients that a user has left.
