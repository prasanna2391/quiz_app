import csv

from django.http import HttpResponse
from django.utils.encoding import smart_str


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=user_scores.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # for excel to be able to open it.
    writer.writerow([
        smart_str(u"User"),
        smart_str(u"Quiz"),
        smart_str(u"Score"),
        smart_str(u"Is Completed"),
    ])
    csv_data = []
    for obj in queryset:
        csv_data.append([
            smart_str(obj.user),
            smart_str(obj.quiz),
            smart_str(obj.correct_answers),
            smart_str(obj.completed),
        ])
    writer.writerows(csv_data)
    return response
    
export_to_csv.short_description = u"Export to csv"
