from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.storage_information_view import format_duration


def passcard_info_view(request, passcode):
  passcard = Passcard.objects.all()
  this_passcard_visits = []
  visits = Visit.objects.filter(passcard__passcode=passcode)
  for visited in visits:
    is_strange = visited.is_visit_long()
    sec_inside = visited.get_duration()
    duration = format_duration(sec_inside, visited)
    this_passcard_visits.append({
      "entered_at": visited.entered_at,
      "duration": duration,
      "is_strange": is_strange
    })
  context = {
    "passcard": passcard,
    "this_passcard_visits": this_passcard_visits
}
  return render(request, 'passcard_info.html', context)
