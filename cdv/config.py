from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = 'cdv'

ADD_PERMISSIONS = {
    "House": "cdv: Add House",
}

setDefaultRoles(
    ADD_PERMISSIONS["House"],
    ('Manager', 'Owner', 'Site Administrator', 'Contributor', )
)
