import flask
from managers import renderManager, taskManager, agents


LIBRA = flask.Flask("LIBRA")

render_manager = renderManager()
task_manager = taskManager()
task_manager.remove_task("write a blogpost")
task_manager.add_task('{"TASK" : "make indomie"}')
'''
@LIBRA.route("/render/jenesis", methods = ["POST","GET"])
def handleJenesisRender():
    if flask.request.method == "POST":
        task = flask.request.headers.get("task")
        render_manager.set_task(agents().JENESIS, task)
        return "finis"

    elif flask.request.method == "GET":
        render_data = flask.make_response()
        render_data.headers["task"] = render_manager.get_task(agents().JENESIS)

        return render_data

@LIBRA.route("/tasklist", methods = ["POST", "GET"])
def handleJenesisTaskList():
    if flask.request.method == "POST":
        tasklist =
        
    if flask.request.method == "GET":
    

LIBRA.run(port = 10000, debug=True)
'''