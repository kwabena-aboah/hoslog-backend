from rest_framework import serializers
from . models import Client

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
                

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Client
        fields = ['id','name_of_customer', 'phone_number', 'test_provided',
                  'price', 'referral_name', 'discount', 'amount_given', 'provided_test_results',
                  'date_of_arrival', 'user']


class ChartSerializer(DynamicFieldsModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Client
        fields = ['id', 'name_of_customer', 'date_of_arrival', 'user']