from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.core.paginator import EmptyPage, InvalidPage, Paginator

from .models import Loans, TestLoans, Author, Book
from .forms import TestLoansForm


class TestLoanAdmin(admin.ModelAdmin):
    form = TestLoansForm


class InlineChangeList(object):
    can_show_all = True
    multi_page = True
    get_query_string = ChangeList.__dict__['get_query_string']

    def __init__(self, request, page_num, paginator):
        self.show_all = 'all' in request.GET
        self.page_num = page_num
        self.paginator = paginator
        self.result_count = paginator.count
        self.params = dict(request.GET.items())


class BookAdmin(admin.TabularInline):
    model = Book
    show_change_link = True
    per_page = 2
    template = 'admin/tabular_paginated.html'
    suit_classes = 'suit-tab suit-tab-general'

    def get_formset(self, request, obj=None, **kwargs):
        formset_class = super(BookAdmin, self).get_formset(request, obj, **kwargs)

        class PaginationFormSet(formset_class):
            def __init__(self, *args, **kwargs):
                super(PaginationFormSet, self).__init__(*args, **kwargs)

                qs = self.queryset
                paginator = Paginator(qs, self.per_page)
                try:
                    page_num = int(request.GET.get('p', '0'))
                except ValueError:
                    page_num = 0

                try:
                    page = paginator.page(page_num + 1)
                except (EmptyPage, InvalidPage):
                    page = paginator.page(paginator.num_pages)

                self.cl = InlineChangeList(request, page_num, paginator)
                self.paginator = paginator

                if self.cl.show_all:
                    self._queryset = qs
                else:
                    self._queryset = page.object_list

        PaginationFormSet.per_page = self.per_page
        return PaginationFormSet


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [BookAdmin]

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name']
        }),
        # ('Architecture', {
        #     'classes': ('suit-tab', 'suit-tab-info',),
        #     'fields': []
        # }
        #  ),
    ]
    # (TAB_NAME, TAB_TITLE)
    suit_form_tabs = (('general', 'General'), ('info', 'Info'))
    suit_form_includes = (
        # ('admin/examples/country/custom_include.html', 'middle', 'cities'),
        ('admin/info.html', 'middle', 'info'),
    )

admin.site.register(Loans)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(TestLoans, TestLoanAdmin)
