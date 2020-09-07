from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def format_duration(sec_inside, visited):
  hours_inside = int(sec_inside // 3600)
  minutes_inside = int((sec_inside % 3600) // 60)
  seconds_inside = int(sec_inside % 60)
  return f'{hours_inside}:{minutes_inside}:{seconds_inside}'


def storage_information_view(request):
  non_closed_visits = []
  visits = Visit.objects.filter(leaved_at=None)
  for visited in visits:
    entered_at = localtime(visited.entered_at)
    sec_inside = visited.get_duration()
    time_inside = format_duration(sec_inside, visited)
    is_strange = visited.is_visit_long()
    non_closed_visits.append({'is_strange': is_strange,
                   'who_entered': visited.passcard,
                   'entered_at': entered_at,
                   'duration': time_inside
                   })
  context = {
      "non_closed_visits": non_closed_visits,
  }
  return render(request, 'storage_information.html', context)
