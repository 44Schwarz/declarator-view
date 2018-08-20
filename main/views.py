from django.shortcuts import render_to_response, HttpResponse, render
from .models import Office, Document, DocumentFile
from django.template import RequestContext


# Create your views here.
def show_table(request):
    return render_to_response('declarator/table.html', {'nodes': Office.objects.all()}, RequestContext(request))


def offices(request, of_id):
    """
    Cases:
    1. No declaration exists - no mark
    2. There are some declarations, but there aren't any files in any of them - empty mark
    3. There are declarations, but not all of them have files (file is None or doesn't exist) - half-filled mark
    4. There are declarations, all with files - filled mark
    """

    offices = Office.objects.get(pk=of_id).get_children()
    years = tuple(range(2017, 2008, -1))
    data = dict()

    for of in offices:
        data[of] = []
        for year in years:
            docs = Document.objects.filter(office=of.id, income_year=year)

            if docs.count() == 0:
                data[of].append('none')
                continue
            any_files, all_files = False, True
            for doc in docs:
                if doc.check_any_files_exist():
                    any_files = True
                if not doc.check_all_files_exist():
                    all_files = False

            if not any_files:
                data[of].append('blank')
            elif not all_files:
                data[of].append('half')
            elif all_files:
                data[of].append('filled')

    return render(request, 'declarator/office.html', context={'data': data,
                                                              'name': Office.objects.get(pk=of_id).name,
                                                              'years': years,
                                                              })
