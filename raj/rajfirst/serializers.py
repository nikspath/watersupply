from rest_framework import serializers
from .models import rajuserfirst

class firstserialize(serializers.ModelSerializer):
	class Meta:
		model=rajuserfirst
		fields='__all__'


