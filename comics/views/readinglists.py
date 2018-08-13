from functools import reduce
import operator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView

from comics.models import ReadingLists


PAGINATE = 30


class ReadingListsList(LoginRequiredMixin, ListView):
    model = ReadingLists
    paginate_by = PAGINATE


class ReadingListsDetail(LoginRequiredMixin, DetailView):
    model = ReadingLists

    def get_context_data(self, **kwargs):
        context = super(ReadingListsDetail, self).get_context_data(**kwargs)
        readinglists = self.get_object()
        context['issue_list'] = (
            readinglists.issues.all()
            .select_related('series')
            .only('slug', 'cover', 'number', 'status', 'series__name')
        )
        return context


class SearchReadingListsList(ReadingListsList):

    def get_queryset(self):
        result = super(SearchReadingListsList, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)))

        return result
