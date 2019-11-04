from rest_framework import serializers

from .models import SKU, GoodsCategory

class SKUSerializer(serializers.ModelSerializer):
    """
    SKU序列器
    """
    user_id = serializers.CharField(source='user_id.nickname')
    # if user_id is "null":
    #     user_id = serializers.CharField(source='user_id.mobile')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = SKU
        fields = ('id', 'create_time', 'title', 'game_content', 'category', 'user_id', 'zan_id',
                  'logo_url', 'img1_url', 'img2_url', 'game_file')


class IndexSKU(serializers.ModelSerializer):
    """
    SKU序列器
    """
    class Meta:
        model = SKU
        fields = ('id', 'title', 'logo_url')

class IndexSKUHOT(serializers.ModelSerializer):
    """
    SKU热门序列器
    """
    class Meta:
        model = SKU
        fields = ('id', 'title', 'zan_id')


class Gamecategory(serializers.ModelSerializer):
    """
    游戏分类序列器
    """
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')


class categorySku(serializers.ModelSerializer):
    """
    SKU序列器
    """
    class Meta:
        model = SKU
        # fields = ('id', 'title', 'logo_url')
        fields = ('id', 'create_time', 'title', 'game_content', 'category', 'user_id', 'zan_id',
                  'logo_url', 'img1_url', 'img2_url', 'game_file')