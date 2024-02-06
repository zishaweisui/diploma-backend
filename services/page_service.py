import math

from models import Page


class PageService:
    async def get_page(self, paging, page_func, count_func, *args, **kwargs):
        skip = (paging.page - 1) * paging.page_size
        limit = paging.page_size
        models = await page_func(skip, limit, *args, **kwargs)
        models_count = await count_func(*args, **kwargs)
        page_count = math.ceil(models_count / limit) or 1
        return Page(items=models, page=paging.page, page_count=page_count)
