from easyverein import EasyvereinAPI
from easyverein.models.custom_field import (
    CustomField,
    CustomFieldCreate,
    CustomFieldUpdate,
)


class TestMember:
    def test_create_custom_field(self, ev_connection: EasyvereinAPI):
        custom_field = ev_connection.custom_field.create(
            CustomFieldCreate(name="Test-Field", kind="e", settings_type="t")
        )
        assert isinstance(custom_field, CustomField)
        assert custom_field.name == "Test-Field"

        # Get all custom fields and check that we've got one now
        custom_fields, total_count = ev_connection.custom_field.get()
        assert isinstance(custom_fields, list)
        assert total_count == 1
        assert len(custom_fields) == 1
        assert all(isinstance(f, CustomField) for f in custom_fields)

        # Change the name of the custom field
        cf = ev_connection.custom_field.update(custom_field.id, CustomFieldUpdate(name="Changed-Name"))

        assert isinstance(cf, CustomField)
        assert cf.name == "Changed-Name"

        # Change type to date
        cf = ev_connection.custom_field.update(custom_field.id, CustomFieldUpdate(settings_type="d"))

        assert isinstance(cf, CustomField)
        assert cf.settings_type == "d"

        # Change kind to contact details
        cf = ev_connection.custom_field.update(custom_field.id, CustomFieldUpdate(kind="j"))

        assert isinstance(cf, CustomField)
        assert cf.kind == "j"

        # Delete custom field again
        ev_connection.custom_field.delete(custom_field)

        # Now there should be none left
        custom_fields = ev_connection.custom_field.get()[0]
        assert isinstance(custom_fields, list)
        assert len(custom_fields) == 0
