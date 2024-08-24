# from django.urls import get_resolver, reverse, NoReverseMatch
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class DynamicAPIRootView(APIView):
#     def get(self, request, *args, **kwargs):
#         urlconf = get_resolver()
#         api_urls = {}

#         def get_urls(patterns, prefix=''):
#             for pattern in patterns:
#                 if hasattr(pattern, 'url_patterns'):
#                     # If the pattern is an include() call, recursively process nested patterns
#                     get_urls(pattern.url_patterns, prefix + str(pattern.pattern))
#                 elif hasattr(pattern, 'name') and pattern.name:
#                     try:
#                         # Construct URL for each named pattern
#                         url = reverse(pattern.name)
#                         api_urls[prefix + str(pattern.pattern)] = url
#                     except NoReverseMatch:
#                         # Skip patterns that cannot be reversed
#                         continue

#         # Start URL resolution from the root
#         get_urls(urlconf.url_patterns)
#         return Response(api_urls, status=status.HTTP_200_OK)



# from order.models import GatheredOrders as o1
# from gath_order.models import GatheredOrders


# def test(request):
#     for order in o1.objects.all():
#         nw = GatheredOrders.objects.create(
#             user=order.user,
#             created_at=order.created_at,
#             status=order.status
#         )
#         nw.save()
