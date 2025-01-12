from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Books
from .serializers import BooksSerializer

class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    @action(detail=False, methods=['get'],url_path='search')
    def search_book(self,request):
        """
        Custom action to search for books by title, author, or ISBN.
        """
        query = request.query_params.get('query', '').strip()

        if query is None or query == '':
            books = Books.objects.all()
            serializer = self.get_serializer(books, many=True)
            return Response(serializer.data)

        # Determine the filter based on the query
        if query.isdigit():
            books = Books.objects.filter(isbn__icontains=query)
        else:
            books = Books.objects.filter(title__icontains=query)
        if books.count() == 0:
            books = Books.objects.filter(author__icontains=query)

        # Serialize the results
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
