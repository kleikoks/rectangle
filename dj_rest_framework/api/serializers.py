from rest_framework import serializers
from ..models import WasteUtil, WasteUtilReview

class WasteUtilReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteUtilReview
        exclude = []

class WasteUtilSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = WasteUtilReviewSerializer(many=True)
    # categories = serializers.SlugRelatedField(slug_field='name', read_only=True, Many=True)
    class Meta:
        model = WasteUtil
        exclude = []