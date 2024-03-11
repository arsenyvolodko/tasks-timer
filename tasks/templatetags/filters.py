from django import template

register = template.Library()


@register.filter(name='work_time')
def work_time(task):
    time_ = task.completed - task.created
    hours, remainder = divmod(time_.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if len(str(hours)) == 1:
        hours = f'0{hours}'
    if len(str(minutes)) == 1:
        minutes = f'0{minutes}'

    return f'{hours}:{minutes}'
