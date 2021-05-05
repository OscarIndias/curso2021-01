# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "project_helpdesk_oscarindias",
    'summary': "modulo de tickets",
    "description":"Helpdesk",
    "version": "14.0.1.0",
    "category": "base",
    "website": "https://factorlibre.com/",
    "author": "Oscar Indias",
    "license": "AGPL-3",
    "depends": [
        "project",
    ],
    
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_menu.xml",
        "views/helpdesk_view.xml",
        "data/project_helpdesk_data.xml",
    ],
    
}