from rest_framework import serializers

from algorithms.models import Preset, RequestSkill


class PresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preset
        fields = '__all__'


class RequestSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestSkill
        fields = '__all__'


class AddEditRequestSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestSkill
        exclude = ('preset_id', 'skill_id')