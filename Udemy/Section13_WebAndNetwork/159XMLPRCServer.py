from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    def multiplier_function(x, y):
        return x * y
    server.register_function(multiplier_function, 'multiply')

    # Run the server's main loop
    server.serve_forever()
