def batch_qs(qs, batch_size=1000):
    """
    Returns a (start, end, total, queryset) tuple for each batch in the given
    queryset. Useful when memory is an issue. Picked from djangosnippets.
    """
    if isinstance(qs, QuerySet):
        total = qs.count()
    else:
        total = len(qs)
        
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        yield (start, end, total, qs[start:end])


# Sample code example to access above method        

"""
users = User.objects.filter(email__isnull=False)
recipient_list = AlertNoticiation.objects.filter(user__in=users)
results = {}
for x in recipient_list:
    for _, _, _, qs in batch_qs(users, batch_size=1000):
        for y in qs:
            # Insert computations here
            results[(x, y)] = True # Not that simple, but still
return results
"""