from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from .models import Book
from rest_framework.viewsets import ModelViewSet
@api_view(['GET','POST'])
def book_view(request):

    if request.method=='POST':
        return Response({"message":"Data posted successfully",'data':request.data})
    return Response({'name':'python','author':'Guido','version':'3.6.3'})

'''class BookView(APIView):
    def get(self,request):
        book=Book.objects.all()
        serializer=BookSerializer(book ,many=True)
        return Response(serializer.data)'''

class BookDetailView(RetrieveAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()



