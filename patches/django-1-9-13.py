# in the file django/db/models/fields/related.py
# replace get_default in line 902

def get_default(self):
    "Here we check if the default value is an object and return the to_field if so."
    field_default = super(ForeignKey, self).get_default()
    print('field_default, self.remote_field.model:', field_default, self.remote_field.model)
    if isinstance(self.remote_field.model, unicode) or isinstance(self.remote_field.model, str):
        from django.apps import apps
        app, model = self.remote_field.model.split('.')
        M = apps.get_model(app, model)
    else:
        M = self.remote_field.model
    if isinstance(field_default, M):
        return getattr(field_default, self.target_field.attname)
    return field_default


