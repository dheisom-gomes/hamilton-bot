from . import app, commands


commands.register(app)
app.run()
