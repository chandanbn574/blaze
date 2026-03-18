from tasks import tasks
def delete_task():
    n=int(input("task number:"))
    tasks.pop(n-1)