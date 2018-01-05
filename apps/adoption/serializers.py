from rest_framework.serializers import ModelSerializer
from apps.adoption.models import People
class PeopleSerializer(ModelSerializer):
	class Meta:
		model= People
		fields= ('identityCard', 'name')
		
			