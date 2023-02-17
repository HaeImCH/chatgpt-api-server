#IMPORT SETTINGS
import settings.Settings as Settings

from api.ChatGPT_Server import app

if __name__ == "__main__":
    #FLASK ONLY IMPLEMENATION
    #app.run(host=Settings.API_HOST, port=Settings.API_PORT, threaded=True)
    
    #HYPERCORN IMPLEMENTATION
    # pip install hypercorn[uvloop]
    """
    from hypercorn.config import Config
    from hypercorn.asyncio import serve
    from hypercorn.middleware import AsyncioWSGIMiddleware
    app = AsyncioWSGIMiddleware(app)
    config = Config()
    config.bind = [f"{Settings.API_HOST}:{Settings.API_PORT}"]
    config.worker_class = "asyncio" # try "uvloop" later
    config.h2_max_concurrent_streams = 10
    asyncio.run(serve(app, config))
    """

    #UVICORN IMPLEMENTATION
    #pip install uvicorn asgiref    
    import uvicorn
    from asgiref.wsgi import WsgiToAsgi
    #app = WsgiToAsgi(app) #IF USING workers=Settings.API_WORKERS,
    uvicorn.run(
        WsgiToAsgi(app), #IF NOT USING workers=Settings.API_WORKERS,
        #"app:app", #IF USING workers=Settings.API_WORKERS,
        host=Settings.API_HOST,
        port=Settings.API_PORT,
        limit_concurrency = None,
        #loop="uvloop", #uvloop not supported on Windows
        #workers=Settings.API_WORKERS, #Seems to spawn multiple instances of the app
        server_header=False
    )    

    #GEVENT IMPLEMENTATION
    #pip install gevent
    """
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer((Settings.API_HOST, Settings.API_PORT), app)
    WSGIServer()
    http_server.serve_forever()
    """