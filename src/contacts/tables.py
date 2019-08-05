import django_tables2 as tables


from contacts.models import Contact


class CheckBoxColumnName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class ContactTable(tables.Table):
    selection = CheckBoxColumnName(verbose_name='Send To', accessor='pk')

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'date_registered']
        sequence = ('selection', 'name', 'phone', 'date_registered')
        template_name = 'table/table.html'
