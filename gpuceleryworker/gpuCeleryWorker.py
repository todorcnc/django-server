from celery import Celery

app = Celery("gpuCeleryWorker")
app.config_from_object("celeryconfig")

@app.task
def simple_task():
    return 10