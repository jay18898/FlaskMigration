from db import ma
# Product Schema
class LoginSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'role_id')

# Init schema
login_schema = LoginSchema(strict=True)
logins_schema = LoginSchema(many=True, strict=True)