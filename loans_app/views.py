from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
# Create your views here.


class CreateBookView(APIView):

    def post(self, request):
        response, status = Book.objects.create_book(request.data)
        return Response(response, status=status)