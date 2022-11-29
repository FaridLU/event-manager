from dataclasses import dataclass
from typing import Optional

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Model
from django.db.models.query import QuerySet
from rest_framework import exceptions
from rest_framework.request import Request


@dataclass
class PaginatedData:
    total_number_of_records: int
    current_page_num: int
    next_page_num: Optional[int]
    last_page_num: int
    paginated_instances: QuerySet

    def asdict(self) -> dict:
        return {key: getattr(self, key) for key in self.__annotations__}


def get_paginated_data(model: Model, query_set: QuerySet, request: Request) -> dict:
    total_number_of_records: int = query_set.count()
    current_page_num: int = request.GET.get("page_num", 1)
    page_size: int = request.GET.get("length", query_set.count() or 10)

    paginator = Paginator(query_set, page_size)
    paginated_instances = model.objects.none()
    
    try:
        page_obj = paginator.page(current_page_num)
        paginated_instances = page_obj.object_list
        try:
            next_page_num = None if not page_obj.has_other_pages() else page_obj.next_page_number()
        except:
            next_page_num = None

    except PageNotAnInteger:
        page_obj = paginator.page(1)
        paginated_instances = page_obj.object_list
        next_page_num = page_obj.next_page_number() if page_obj.has_other_pages() else None

    except EmptyPage:
        paginated_instances = model.objects.none()
        next_page_num = None

    last_page_num = paginator.num_pages
        
    return PaginatedData(
        total_number_of_records=total_number_of_records,
        current_page_num=current_page_num,
        next_page_num=next_page_num,
        last_page_num=last_page_num,
        paginated_instances=paginated_instances,
    ).asdict()
