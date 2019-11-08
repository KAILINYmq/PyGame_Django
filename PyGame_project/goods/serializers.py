from rest_framework import serializers

from .models import SKU, GoodsCategory

class SKUSerializer(serializers.ModelSerializer):
    """
    SKU序列器
    """
    user_id = serializers.CharField(source='user_id.nickname')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = SKU
        fields = ('id', 'create_time', 'title', 'game_content', 'category', 'user_id', 'zan_id',
                  'logo_url', 'img1_url', 'img2_url', 'game_file')


class UPGameSKUSerializer(serializers.ModelSerializer):
    """
    UPGameSKU序列器
    """
    class Meta:
        model = SKU
        fields = ('id', 'create_time', 'title', 'game_content', 'category', 'user_id',
                  'logo_url', 'img1_url', 'img2_url', 'game_file')
        extra_kwargs = {
            'zan_id': {
                'read_only': True,
            }
        }

class IndexSKU(serializers.ModelSerializer):
    """
    SKU序列器
    """
    class Meta:
        model = SKU
        fields = ('id', 'title', 'logo_url')


class UserLaunchedserializers(serializers.ModelSerializer):
    """
    游戏待审核接口
    """
    class Meta:
        model = SKU
        fields = ('id', 'title', 'create_time', 'is_launched')


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
        fields = ('id', 'create_time', 'title', 'game_content', 'category', 'user_id', 'zan_id',
                  'logo_url', 'img1_url', 'img2_url', 'game_file')