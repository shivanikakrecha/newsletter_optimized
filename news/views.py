from celery.result import AsyncResult
from .tasks import do_work

def get_progress(request, task_id):
    result = AsyncResult(task_id)
    response_data = {
        'state': result.state,
        'details': result.info,
    }
    return HttpResponse(json.dumps(response_data), content_type='application/json')


def my_view(request):
     # the .delay() call here is all that's needed
     # to convert the function to be called asynchronously
     do_work.delay()
     # we can't say 'work done' here anymore because all we did was kick it off
     return HttpResponse('work kicked off!')


"""
Need to put in javasctipt and template

function updateProgress (progressUrl) {
    fetch(progressUrl).then(function(response) {
        response.json().then(function(data) {
            // update the appropriate UI components
            setProgress(data.state, data.details);
            setTimeout(updateProgress, 500, progressUrl);
        });
    });
}
var progressUrl = '{% url "task_status" task_id %}';  // django template usage
updateProgress(progressUrl);

"""