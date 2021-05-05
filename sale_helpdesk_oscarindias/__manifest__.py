# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "sale_helpdesk_oscarindias",
    'summary': "modulo de tickets",
    "description":"Helpdesk",
    "version": "14.0.1.0",
    "category": "base",
    "website": "https://factorlibre.com/",
    "author": "Oscar Indias",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "helpdesk_oscarindias",
    ],
    
    "data": [
        "views/product_product_view.xml",
        "views/sale_order_view.xml",
        "views/helpdesk_ticket_view.xml",
    ],
    
}