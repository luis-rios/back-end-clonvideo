def get_queryset(self):
    query = {}
    for item in self.request.query_params:
        if item not in ['page_size']:
            continue
        query[item + '__icontains'] = self.request.query_params[item]
    self.queryset = self.queryset.filter(**query)
    return super().get_queryset()