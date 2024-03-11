from django import template

register = template.Library()


@register.filter(name='work_time')
def work_time(task):
    time_ = task.completed - task.created
    hours, remainder = divmod(time_.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours == 0:
        return f'{minutes} м'
    return f'{hours} ч {minutes} м'
