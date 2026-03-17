##warm start
# from flask import Flask, jsonify
# import time
# import os

# app = Flask(__name__)

# START_TIME = time.time()

# @app.route("/")
# def home():

#     uptime = time.time() - START_TIME

#     return jsonify({
#         "message": "serverless performance research",
#         "container_uptime": uptime,
#         "revision": os.getenv("K_REVISION")
#     })


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)


################################################################################



##cold start
# from flask import Flask, jsonify, after_this_request
# import time
# import os

# app = Flask(__name__)

# START_TIME = time.time()

# @app.route("/")
# def home():

#     uptime = time.time() - START_TIME

#     response = {
#         "message": "serverless performance research",
#         "container_uptime": uptime,
#         "revision": os.getenv("K_REVISION")
#     }

#     @after_this_request
#     def shutdown(response):
#         os._exit(0) #force container exit
#         return response

#     return jsonify(response)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)