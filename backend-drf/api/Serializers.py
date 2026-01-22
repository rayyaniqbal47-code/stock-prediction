from rest_framework import serializers

class StockSerializer(serializers.Serializer):
    ticker = serializers.CharField(max_length=20)
    








