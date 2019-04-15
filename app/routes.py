from app import app

@app.route('/')
@app.route('/index')
def index():
    return "index"

@app.route('/hello')
def hello():
    return "Hello World from Ovandi!"

@app.route('/<effect>', methods = 'GET')
def getStrains(effect):
    """
    For an EFFECT (appetite,pain,euphoria etc), returns the list
    of strains with EFFECT as its primary effect
    """
    # THIS WILL NOT WORK YET
    return Strain.query.filter_by(effect = effect)

if __name__ == '__main__':
    app.run()
