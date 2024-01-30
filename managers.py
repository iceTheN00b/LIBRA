import pandas
import json
from agents import agents

class renderManager:

    def __init__(self):
        self.RENDER_FILES = {
            "JENESIS" : "data/renderData/jenesis.json"
        }
        self.setup()

    def set_task(self, render_json, new_task):
        render_data = json.load(open(render_json, "r"))
        render_data["task"] = new_task
        json.dump(render_data, open(render_json, "w"), indent = 2)
        print(f"!SUCESSFULLY UPDATED {render_json.split('/')[-1].split('.json')[0].upper()} TASK TO {new_task}")

    def get_task(self, render_json):
        render_data = json.load(open(render_json, "r"))
        return render_data["task"]

    def setup(self):
        self.set_task(agents().JENESIS, "IDLE")

class taskManager:
    def __init__(self):
        self.TASKLIST : str = "data/taskData/taskList.csv"

    def get_all_tasks(self):
        tasklist =pandas.read_csv(self.TASKLIST)
        return tasklist.to_string(index = False)

    def remove_task(self, task_to_remove):
        tasklist = pandas.read_csv(self.TASKLIST)
        tasklist.drop( tasklist[ tasklist["TASK"] == task_to_remove ].index, inplace = True )
        tasklist.to_csv(self.TASKLIST, index = True)

    def add_task(self, new_task):
        tasklist = pandas.read_csv(self.TASKLIST)
        new_task = json.loads(new_task)
        tasklist.append(new_task, ignore_index = True)
        tasklist.to_csv(self.TASKLIST, index=True)


