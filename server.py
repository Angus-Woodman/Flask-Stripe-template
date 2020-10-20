from flask import Flask, render_template

server = Flask(__name__)

server.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51HdxovB6KrRuwHV6JVCl9dlIU2E4mXA1sdLM6roIZM7o7yaLe5LGniJSyI6qB51eXMq31yz9zPt7SxNHL3Znq5Ak00UBH32TB2'
server.config['STRIPE_SECRET_KEY'] = 'sk_test_51HdxovB6KrRuwHV6gjYobKMwj7PJV5OMzWELD5Y7gXW0vSYfoJ75iZPRIVNTYcTAUV62xBTKrMesMmSnMjrjGtm500y1Djh0MK'


@server.route('/')
def index():
    return render_template('index.html')

@server.route('/thanks')
def thanks():
    return render_template('thanks.html')
