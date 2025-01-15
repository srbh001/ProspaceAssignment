from rest_framework.serializers import ModelSerializer

from utils.models import Order, District, Talluka, Village


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "created_at", "updated_at", "order_type", "entity_name", "user"]
        read_only_fields = ["id", "created_at", "updated_at"]


class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name"]


class VillageSerializer(ModelSerializer):
    class Meta:
        model = Village
        fields = ["id", "name"]


class TallukaSerializer(ModelSerializer):
    class Meta:
        model = Talluka
        fields = ["id", "name"]
