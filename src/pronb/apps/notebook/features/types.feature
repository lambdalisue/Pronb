Feature: of types
    Scenario: NOTEBOOK_TYPE_PUBLIC
        When I access "NOTEBOOK_TYPE_PUBLIC"
        Then I get "public"
    Scenario: NOTEBOOK_TYPE_FRIEND
        When I access "NOTEBOOK_TYPE_FRIEND"
        Then I get "friend"
    Scenario: NOTEBOOK_TYPE_PRIVATE
        When I access "NOTEBOOK_TYPE_PRIVATE"
        Then I get "private"
    Scenario: NOTEBOOK_TYPES
        When I access "NOTEBOOK_TYPES"
        Then I get the following:
            | public | friend | private |
            | public | friend | private |
