from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.core.api.serializers import MessageSerializer
from apps.core.api.utils import Request
from apps.core.models import Message


@api_view(['POST'])
@Request.post
def create_message(request):
    if request.method == 'POST':
        try:
            text = request.data['text']
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        new_msg = Message.objects.create(
            text=text
        )
        serializer = MessageSerializer(new_msg)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@Request.get
def get_message(request, message_id, access_token):
    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if str(access_token) == str(message.access_token):
        text = message.text
        message.is_viewed = True
        message.save()

        return Response({'text': text}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
