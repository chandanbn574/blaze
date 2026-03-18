from tasks import tasks
def view_task():
    for i,t in enumerate(tasks):
        print(i+1,t)