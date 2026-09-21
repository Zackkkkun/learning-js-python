tasks = []

def add_task(title):
    task = {"title":title, "done":False}
    tasks.append(task)

add_task("learn arrays")
add_task("learn functions")
add_task("learn python dictionary")

print(tasks)