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

    def validate(self, attrs):
        #  判断是否有重复的游戏
        try:
            if SKU.objects.get(title=attrs.get('title')):
                raise serializers.ValidationError('当前游戏已存在!')
        except SKU.DoesNotExist:
            pass

        if str(attrs.get('logo_url'))[-3:] not in ['png', 'jpg', 'jpeg']:
            raise serializers.ValidationError('请上传正确的图片!')
        return attrs

    def validate_game_file(self, value):
        #  判断文件格式
        if str(value)[-3:] not in ['rar', 'zip', 'jar']:
            raise serializers.ValidationError('请上传正确的游戏文件！')
        return value

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