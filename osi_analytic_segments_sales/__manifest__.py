# Copyright (C) 2019 - TODAY, Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "OSI Analytic Segments Sales",
    "version": "14.0.1.0.0",
    "license": "LGPL-3",
    "summary": "Additional segments for analytic accounts for Sales",
    "author": "Open Source Integrators",
    "maintainer": "Open Source Integrators",
    "website": "https://github.com/ursais/osi-addons",
    "category": "Analytic Accounting",
    "depends": [
        "stock_account",
        "sale_management",
        "osi_analytic_segments",
    ],
    "data": [
        "views/sale_order_view.xml",
    ],
    "installable": True,
}
