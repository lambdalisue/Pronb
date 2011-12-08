Feature: Attribute test of Notebook model
    To avoid mismatch of attribute name

    Scenario: Notebook.objects.published
        When annonymous user access the "published" method of Notebook.objects
        Then he get queryset of all notebook which type is public

    Scenario: publish method (authenticated)
        When authenticated user access the "published" method
        Then he get queryset of all notebook which type is public
        And the queryset of all notebook which type is public are not own
        And he get queryset of all notebook which he have 
        And the queryset of all notebook which he have is assumed is_draft or is_removed is not True
